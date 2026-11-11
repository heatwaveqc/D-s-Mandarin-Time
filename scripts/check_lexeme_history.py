#!/usr/bin/env python3
"""Enforce lexeme ID non-reuse against main when GitHub runs a PR check."""
from __future__ import annotations
import csv
import io
import os
import subprocess
from pathlib import Path
from validate_lexicon import REGISTRY_COLUMNS, check_history

REGISTRY = "research/lexeme-id-registry.csv"


def main() -> int:
    base = os.environ.get("GITHUB_BASE_REF")
    if not base:
        print("Lexeme history: no base branch set; local static validation applies.")
        return 0
    if not base.replace("-", "").replace("_", "").isalnum():
        print("Lexeme history: unsafe base ref")
        return 1
    fetched = subprocess.run(["git", "fetch", "--no-tags", "origin",
                              f"refs/heads/{base}:refs/remotes/origin/{base}"],
                             capture_output=True, text=True, check=False)
    if fetched.returncode:
        print("Lexeme history: unable to fetch base branch", fetched.stderr)
        return 1
    old = subprocess.run(["git", "show", f"origin/{base}:{REGISTRY}"],
                         capture_output=True, text=True, check=False)
    if old.returncode:
        if "does not exist in" in old.stderr or "exists on disk, but not in" in old.stderr:
            print("Lexeme history: initial registry introduction; no previous allocation.")
            return 0
        print("Lexeme history: unable to read previous registry", old.stderr)
        return 1
    current = Path(REGISTRY)
    if not current.is_file():
        print("Lexeme history: proposed registry is missing")
        return 1
    def parse_csv(text: str):
        reader = csv.DictReader(io.StringIO(text))
        if reader.fieldnames != REGISTRY_COLUMNS:
            raise ValueError("registry header mismatch")
        return list(reader)
    try:
        issues = check_history(parse_csv(old.stdout), parse_csv(current.read_text(encoding="utf-8")))
    except (ValueError, UnicodeError, csv.Error) as exc:
        print("Lexeme history:", exc)
        return 1
    for issue in issues:
        print("ERROR:", issue)
    if issues:
        return 1
    print("PASS: existing lexeme IDs remain reserved; new allocations are monotonic")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
