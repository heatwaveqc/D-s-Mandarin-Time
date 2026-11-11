#!/usr/bin/env python3
"""Validate lexical identity and evidence files without claiming linguistic accuracy."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ID_RE = re.compile(r"^lx-[0-9]{6}$")
SOURCE_RE = re.compile(r"^[a-z][a-z0-9-]*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
VALID_BANDS = {"fundamental", "high-use", "high-availability", "wuxia-specialist"}
REGISTRY_COLUMNS = ["lexeme_id", "tiddler_path", "status", "assigned_batch", "notes"]
EVIDENCE_COLUMNS = ["evidence_id", "lexeme_id", "source_id", "claim_type", "claim_value",
                    "review_status", "reviewed_by", "reviewed_on", "notes"]
CLAIM_TYPES = {"form", "pronunciation", "sense", "register", "frequency", "hsk",
               "availability", "genre", "band"}
REVIEW_STATES = {"candidate", "checked", "verified"}
SOURCE_STATES = {"editorial-original", "reference-only", "research-reference-only",
                 "not-yet-approved", "redistribution-approved"}


def read_csv(path: Path, columns: list[str], errors: list[str]) -> list[dict[str, str]]:
    if not path.is_file():
        errors.append(f"Missing lexical research file {path}")
        return []
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != columns:
                errors.append(f"{path}: expected columns {columns}, got {reader.fieldnames}")
                return []
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{path}: unable to parse CSV: {exc}")
        return []
    for i, row in enumerate(rows, start=2):
        if None in row or any(value is None for value in row.values()):
            errors.append(f"{path}:{i}: malformed CSV row")
    return rows


def parse_headers(path: Path) -> dict[str, str]:
    """Metadata only; the existing wiki validator handles full tiddler syntax."""
    header = path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n\n", 1)[0]
    fields = {}
    for line in header.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value.strip()
    return fields


def validate(project_root: Path = PROJECT_ROOT) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    research = project_root / "research"
    records = read_csv(research / "lexeme-id-registry.csv", REGISTRY_COLUMNS, errors)
    evidence_rows = read_csv(research / "lexical-evidence.csv", EVIDENCE_COLUMNS, errors)
    source_path = research / "lexical-sources.json"
    try:
        data = json.loads(source_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("schema_version") != 1:
            raise ValueError("expected object with schema_version = 1")
        entries = data.get("sources")
        if not isinstance(entries, list):
            raise ValueError("sources must be an array")
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"{source_path}: invalid source registry: {exc}")
        entries = []

    sources: dict[str, dict] = {}
    for source in entries:
        if not isinstance(source, dict):
            errors.append(f"{source_path}: source must be an object")
            continue
        sid = source.get("id")
        if not isinstance(sid, str) or not SOURCE_RE.fullmatch(sid):
            errors.append(f"{source_path}: invalid source id {sid!r}")
            continue
        if sid in sources:
            errors.append(f"{source_path}: duplicate source id {sid}")
            continue
        sources[sid] = source
        if source.get("reuse_status") not in SOURCE_STATES:
            errors.append(f"{sid}: invalid reuse_status")
        for required in ("kind", "source_url", "license", "accessed"):
            if not source.get(required):
                errors.append(f"{sid}: missing source {required}")
        if source.get("reuse_status") == "redistribution-approved":
            if not source.get("release") or not SHA256_RE.fullmatch(source.get("sha256") or ""):
                errors.append(f"{sid}: approved source requires frozen release and SHA-256")

    id_to_record: dict[str, dict[str, str]] = {}
    path_to_id: dict[str, str] = {}
    for row in records:
        lid = row.get("lexeme_id") or ""
        path = row.get("tiddler_path") or ""
        status = row.get("status") or ""
        if not ID_RE.fullmatch(lid):
            errors.append(f"Registry: invalid lexeme ID {lid!r}")
        if lid in id_to_record:
            errors.append(f"Registry: duplicated lexeme ID {lid!r}")
        id_to_record[lid] = row
        if status not in {"active", "retired"}:
            errors.append(f"Registry: {lid}: invalid status {status!r}")
        if not row.get("assigned_batch"):
            errors.append(f"Registry: {lid}: missing assigned_batch")
        if status == "active":
            parts = Path(path).parts
            if (not path.startswith("tiddlers/Vocabulary/") or not path.endswith(".tid")
                    or ".." in parts or path.startswith("/")
                    or len(parts) < 3):
                errors.append(f"Registry: {lid}: unsafe tiddler path {path!r}")
            if path in path_to_id:
                errors.append(f"Registry: {path!r} registered twice")
            path_to_id[path] = lid
        elif path:
            errors.append(f"Registry: retired {lid} must have empty tiddler_path")

    evidence: dict[str, dict[str, str]] = {}
    for row in evidence_rows:
        eid = row.get("evidence_id") or ""
        lid = row.get("lexeme_id") or ""
        sid = row.get("source_id") or ""
        kind = row.get("claim_type") or ""
        status = row.get("review_status") or ""
        if not eid or eid in evidence:
            errors.append(f"Evidence: blank or duplicate ID {eid!r}")
        evidence[eid] = row
        if lid not in id_to_record or id_to_record[lid].get("status") != "active":
            errors.append(f"Evidence {eid}: unknown/retired lexeme ID {lid!r}")
        if sid not in sources:
            errors.append(f"Evidence {eid}: unknown source {sid!r}")
        if kind not in CLAIM_TYPES:
            errors.append(f"Evidence {eid}: unknown claim type {kind!r}")
        if status not in REVIEW_STATES:
            errors.append(f"Evidence {eid}: invalid review state {status!r}")
        if status == "verified" and not (row.get("reviewed_by") and row.get("reviewed_on")):
            errors.append(f"Evidence {eid}: verified claim requires reviewer and review date")
        if not row.get("claim_value"):
            errors.append(f"Evidence {eid}: missing claim value")
        if kind == "band" and row.get("claim_value") not in VALID_BANDS:
            errors.append(f"Evidence {eid}: unsupported lexical band")
        if kind in {"frequency", "hsk"} and row.get("claim_value"):
            source = sources.get(sid, {})
            if (source.get("reuse_status") != "redistribution-approved"
                    or not source.get("release")
                    or not SHA256_RE.fullmatch(source.get("sha256") or "")):
                errors.append(f"Evidence {eid}: public {kind} value requires approved, frozen source {sid!r}")

    tiddlers = project_root / "tiddlers"
    seen: dict[str, str] = {}
    word_count = 0
    for path in sorted(tiddlers.rglob("*.tid")):
        try:
            fields = parse_headers(path)
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: cannot read tiddler: {exc}")
            continue
        if fields.get("mandarin-kind") != "vocabulary":
            continue
        word_count += 1
        relative = path.relative_to(project_root).as_posix()
        lid = fields.get("mandarin-lexeme-id", "")
        if not ID_RE.fullmatch(lid):
            errors.append(f"{relative}: missing/invalid mandarin-lexeme-id {lid!r}")
        if lid in seen:
            errors.append(f"{relative}: duplicate lexeme ID {lid!r} also at {seen[lid]}")
        seen[lid] = relative
        registered = id_to_record.get(lid)
        if registered is None or registered.get("status") != "active":
            errors.append(f"{relative}: lexeme {lid!r} not active in registry")
        elif registered.get("tiddler_path") != relative:
            errors.append(f"{relative}: registry points {lid} to {registered['tiddler_path']!r}")
        source_ids = fields.get("mandarin-source-ids", "").split()
        if not source_ids:
            errors.append(f"{relative}: missing mandarin-source-ids")
        if len(set(source_ids)) != len(source_ids):
            errors.append(f"{relative}: duplicate mandarin-source-ids")
        for sid in source_ids:
            if sid not in sources:
                errors.append(f"{relative}: unknown source ID {sid!r}")
        for label, metadata, claim_kind in (
            ("mandarin-band-evidence-id", "mandarin-lexical-band", "band"),
            ("mandarin-frequency-evidence-id", "mandarin-frequency-rank", "frequency"),
            ("mandarin-hsk-evidence-id", "mandarin-hsk-level", "hsk"),
        ):
            asserted = fields.get(metadata)
            evid_id = fields.get(label)
            if asserted and not evid_id:
                errors.append(f"{relative}: {metadata} requires {label}")
            if not evid_id:
                continue
            row = evidence.get(evid_id)
            if (not row or row.get("lexeme_id") != lid
                    or row.get("claim_type") != claim_kind
                    or row.get("review_status") != "verified"):
                errors.append(f"{relative}: {label} must reference verified {claim_kind} evidence for {lid}")
            elif asserted and asserted != row.get("claim_value"):
                errors.append(f"{relative}: {metadata} differs from evidence {evid_id}")
        if fields.get("mandarin-lexical-band") and fields["mandarin-lexical-band"] not in VALID_BANDS:
            errors.append(f"{relative}: invalid lexical band")
        for name in ("mandarin-frequency-zipf", "mandarin-frequency-score"):
            if fields.get(name) and not fields.get("mandarin-frequency-evidence-id"):
                errors.append(f"{relative}: {name} requires frequency evidence")

    for path, lid in path_to_id.items():
        if seen.get(lid) != path:
            errors.append(f"Registry: active {lid} does not match a vocabulary tiddler at {path}")
    return errors, {"lexemes": word_count, "registered": len(id_to_record),
                    "sources": len(sources), "evidence": len(evidence)}


def check_history(old: list[dict[str, str]], new: list[dict[str, str]]) -> list[str]:
    """Guard append-only IDs across PRs; changing a tiddler path needs an explicit move note."""
    problems = []
    before = {row["lexeme_id"]: row for row in old}
    after = {row["lexeme_id"]: row for row in new}
    largest = max((int(k[3:]) for k in before if ID_RE.fullmatch(k)), default=0)
    new_numbers = sorted(int(k[3:]) for k in after if k not in before and ID_RE.fullmatch(k))
    if new_numbers and new_numbers != list(range(largest + 1, largest + len(new_numbers) + 1)):
        problems.append("New lexeme IDs must be allocated sequentially after the previous maximum")
    for lid, previous in before.items():
        current = after.get(lid)
        if current is None:
            problems.append(f"Previously allocated lexeme ID {lid} was removed (retire it instead)")
        elif previous.get("status") == "retired" and current.get("status") != "retired":
            problems.append(f"Retired lexeme ID {lid} cannot be reactivated")
        elif previous.get("tiddler_path") != current.get("tiddler_path"):
            if not (current.get("notes") or "").startswith("moved:"):
                if current.get("status") != "retired":
                    problems.append(f"Lexeme {lid} moved without a 'moved:' audit note")
    return problems
