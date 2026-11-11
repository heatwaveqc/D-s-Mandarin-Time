#!/usr/bin/env python3
"""Publish a planned lexeme, or allocate an ID for a genuinely new vocabulary .tid.

Planned IDs are reserved in the research phase and must be reused on publication.
Selection and provenance evidence remain outside learner-facing TiddlyWiki records.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from validate_lexicon import ID_RE, REGISTRY_COLUMNS, PROJECT_ROOT, SELECTION_COLUMNS


def read_rows(path: Path, expected: list[str]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != expected:
            raise ValueError(f"Unexpected CSV columns in {path}")
        return list(reader)


def register(root: Path, relative_path: str, batch: str,
             dry_run: bool = False, planned_id: str | None = None) -> str:
    path = Path(relative_path)
    if (path.is_absolute() or ".." in path.parts
            or len(path.parts) < 3 or path.parts[:2] != ("tiddlers", "Vocabulary")
            or path.suffix != ".tid"):
        raise ValueError("Expected a relative path beneath tiddlers/Vocabulary/*.tid")
    if not batch or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.-]*", batch):
        raise ValueError("Batch name is required (letters, numbers, period, dash, underscore)")
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
        raise ValueError("Research provenance belongs in the external evidence ledger")
    registry = root / "research" / "lexeme-id-registry.csv"
    rows = read_rows(registry, REGISTRY_COLUMNS)
    if any(r["tiddler_path"] == path.as_posix() for r in rows):
        raise ValueError("Tiddler path is already registered")

    if planned_id is not None:
        if not ID_RE.fullmatch(planned_id):
            raise ValueError("Invalid planned lexical ID")
        matches = [r for r in rows if r["lexeme_id"] == planned_id]
        if len(matches) != 1 or matches[0]["status"] != "planned":
            raise ValueError("Requested ID is not uniquely registered as planned")
        selected = read_rows(root / "research" / "lexical-selection.csv", SELECTION_COLUMNS)
        chosen = [r for r in selected if r["lexeme_id"] == planned_id]
        if len(chosen) != 1:
            raise ValueError("Planned ID must have exactly one selection-roster row")
        for field, col in (("mandarin-hanzi", "simplified"), ("mandarin-pinyin", "pinyin")):
            raw = re.search(rf"^{re.escape(field)}: (.+)$", header, re.MULTILINE)
            if raw is None or raw.group(1).strip() != chosen[0][col]:
                raise ValueError(f"{field} must match the frozen selection for {planned_id}")
        allocated = planned_id
    else:
        numeric = [int(r["lexeme_id"][3:]) for r in rows if ID_RE.fullmatch(r["lexeme_id"])]
        allocated = f"lx-{max(numeric, default=0) + 1:06d}"

    new_header = header.replace("mandarin-kind: vocabulary",
                                f"mandarin-kind: vocabulary\nmandarin-lexeme-id: {allocated}", 1)
    if dry_run:
        return allocated
    if planned_id is not None:
        record = matches[0]
        record["tiddler_path"] = path.as_posix()
        record["status"] = "active"
        record["notes"] = "published: " + batch + ("; " + record["notes"] if record["notes"] else "")
    else:
        rows.append({"lexeme_id": allocated, "tiddler_path": path.as_posix(),
                     "status": "active", "assigned_batch": batch, "notes": ""})
    target.write_text(new_header + "\n\n" + body, encoding="utf-8")
    with registry.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=REGISTRY_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return allocated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Relative path to an unpublished vocabulary .tid without an ID")
    parser.add_argument("--batch", required=True, help="Production batch identifier")
    parser.add_argument("--lexeme-id", help="An already planned ID from the approved selection roster")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        allocated = register(PROJECT_ROOT, args.path, args.batch,
                             dry_run=args.dry_run, planned_id=args.lexeme_id)
    except (OSError, ValueError, KeyError, csv.Error) as exc:
        parser.error(str(exc))
    print(f"{allocated} → {args.path}" + (" (dry run)" if args.dry_run else " (registered)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
