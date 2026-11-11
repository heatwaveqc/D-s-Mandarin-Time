#!/usr/bin/env python3
"""Allocate a never-reused vocabulary ID and register a new .tid in one operation.

Use from a local checkout *before* opening the import PR. GitHub-only editors
can make equivalent paired .tid/registry changes manually.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from validate_lexicon import ID_RE, REGISTRY_COLUMNS, PROJECT_ROOT


def register(root: Path, relative_path: str, batch: str,
             source_ids: str = "curriculum-editorial", dry_run: bool = False) -> str:
    path = Path(relative_path)
    if (path.is_absolute() or ".." in path.parts
            or len(path.parts) < 3 or path.parts[:2] != ("tiddlers", "Vocabulary")
            or path.suffix != ".tid"):
        raise ValueError("Expected a relative path beneath tiddlers/Vocabulary/*.tid")
    if not batch or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.-]*", batch):
        raise ValueError("Batch name is required (letters, numbers, period, dash, underscore)")
    sources = json.loads((root / "research" / "lexical-sources.json").read_text(encoding="utf-8"))
    known_sources = {source["id"] for source in sources["sources"]}
    requested = source_ids.split()
    if not requested or any(s not in known_sources for s in requested):
        raise ValueError("All source IDs must exist in the source registry")
    target = root / path
    content = target.read_text(encoding="utf-8")
    if "\n\n" not in content:
        raise ValueError("Tiddler header must be separated from the body by a blank line")
    header, body = content.split("\n\n", 1)
    if not re.search(r"^mandarin-kind: vocabulary$", header, re.MULTILINE):
        raise ValueError("Target is not a vocabulary tiddler")
    if re.search(r"^mandarin-lexeme-id:", header, re.MULTILINE):
        raise ValueError("Tiddler already has a lexical ID; do not reallocate it")
    if re.search(r"^mandarin-source-ids:", header, re.MULTILINE):
        existing = re.search(r"^mandarin-source-ids: (.*)$", header, re.MULTILINE).group(1)
        if not existing or any(s not in known_sources for s in existing.split()):
            raise ValueError("Tiddler source IDs are invalid")
        add_source = ""
    else:
        add_source = "\nmandarin-source-ids: " + " ".join(requested)
    registry = root / "research" / "lexeme-id-registry.csv"
    with registry.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != REGISTRY_COLUMNS:
            raise ValueError("Registry column mismatch")
        rows = list(reader)
    if any(r["tiddler_path"] == path.as_posix() for r in rows):
        raise ValueError("Tiddler path is already registered")
    numeric = [int(r["lexeme_id"][3:]) for r in rows if ID_RE.fullmatch(r["lexeme_id"])]
    new_id = f"lx-{max(numeric, default=0) + 1:06d}"
    insertion = f"mandarin-kind: vocabulary\nmandarin-lexeme-id: {new_id}{add_source}"
    new_header = header.replace("mandarin-kind: vocabulary", insertion, 1)
    if new_header == header:
        raise ValueError("Failed to insert lexical ID")
    if dry_run:
        return new_id
    rows.append({"lexeme_id": new_id, "tiddler_path": path.as_posix(),
                 "status": "active", "assigned_batch": batch, "notes": ""})
    target.write_text(new_header + "\n\n" + body, encoding="utf-8")
    with registry.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=REGISTRY_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return new_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Relative path to a new vocabulary .tid without an ID")
    parser.add_argument("--batch", required=True, help="Provenance batch identifier")
    parser.add_argument("--source-ids", default="curriculum-editorial",
                        help="Space-separated source IDs from lexical-sources.json")
    parser.add_argument("--dry-run", action="store_true", help="Show the next ID without editing")
    args = parser.parse_args()
    try:
        new_id = register(PROJECT_ROOT, args.path, args.batch, args.source_ids, args.dry_run)
    except (OSError, ValueError, KeyError, csv.Error, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(f"{new_id} → {args.path}" + (" (dry run)" if args.dry_run else " (registered)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
