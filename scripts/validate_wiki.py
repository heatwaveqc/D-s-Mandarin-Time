#!/usr/bin/env python3
"""Validate the modular Mandarin TiddlyWiki content before publishing."""
from __future__ import annotations
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIDDLERS = ROOT / "tiddlers"
VALID_KINDS = {"navigation", "roadmap", "grammar", "vocabulary",
               "character", "lesson", "reading", "exercise"}
REQUIRED_WORD = ("mandarin-hanzi", "mandarin-pinyin",
                 "mandarin-gloss", "mandarin-pos")
REQUIRED_CHARACTER = ("mandarin-hanzi", "mandarin-pinyin", "mandarin-gloss")
VALID_LEXICAL_BANDS = {"fundamental", "high-use", "high-availability", "wuxia-specialist"}
LIST_ITEM_RE = re.compile(r"\[\[([^\]]+)\]\]|([^\s]+)")
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def parse_tiddler(text: str, path: str = "") -> tuple[dict[str, str], str]:
    """Return text-header fields and body. The first blank line ends headers."""
    text = text.replace("\r\n", "\n")
    if "\n\n" not in text:
        raise ValueError(f"{path}: no blank line after .tid headers")
    header, body = text.split("\n\n", 1)
    fields = {}
    for line in header.splitlines():
        if ": " not in line:
            raise ValueError(f"{path}: malformed field: {line!r}")
        key, value = line.split(": ", 1)
        if key in fields:
            raise ValueError(f"{path}: duplicate field {key!r}")
        fields[key] = value.strip()
    if not fields.get("title"):
        raise ValueError(f"{path}: missing title")
    return fields, body


def title_list(value: str) -> list[str]:
    return [a or b for a, b in LIST_ITEM_RE.findall(value)]


def detect_cycles(edges: dict[str, list[str]]) -> list[list[str]]:
    seen, active, stack, cycles = set(), set(), [], []

    def walk(node: str) -> None:
        seen.add(node)
        active.add(node)
        stack.append(node)
        for dep in edges.get(node, []):
            if dep not in seen:
                walk(dep)
            elif dep in active:
                cycles.append(stack[stack.index(dep):] + [dep])
        stack.pop()
        active.remove(node)

    for item in edges:
        if item not in seen:
            walk(item)
    return cycles


def validate(root: Path = TIDDLERS) -> tuple[list[str], dict[str, int]]:
    errors = []
    found: dict[str, tuple[dict[str, str], str, Path]] = {}
    counts = defaultdict(int)
    paths = sorted(root.rglob("*.tid"))
    if not paths:
        return [f"No .tid records in {root}"], {}

    for p in paths:
        try:
            fields, body = parse_tiddler(p.read_text(encoding="utf-8"), str(p))
        except (OSError, ValueError) as exc:
            errors.append(str(exc))
            continue
        title = fields["title"]
        if title in found:
            errors.append(f"Duplicate title {title!r} in {p} and {found[title][2]}")
        found[title] = (fields, body, p)
        if title.startswith("$:/"):
            counts["system"] += 1
            continue
        kind = fields.get("mandarin-kind")
        if kind not in VALID_KINDS:
            errors.append(f"{p}: unknown/missing mandarin-kind {kind!r}")
            continue
        counts[kind] += 1
        if not fields.get("mandarin-level"):
            errors.append(f"{p}: missing mandarin-level")
        if kind == "vocabulary":
            for key in REQUIRED_WORD:
                if not fields.get(key):
                    errors.append(f"{p}: missing {key}")
            lexical_band = fields.get("mandarin-lexical-band")
            if lexical_band and lexical_band not in VALID_LEXICAL_BANDS:
                errors.append(f"{p}: unsupported mandarin-lexical-band {lexical_band!r}")
        if kind == "character":
            for key in REQUIRED_CHARACTER:
                if not fields.get(key):
                    errors.append(f"{p}: missing {key}")
        if kind == "lesson" and not fields.get("mandarin-summary"):
            errors.append(f"{p}: missing lesson summary")
        if fields.get("type") != "text/vnd.tiddlywiki":
            errors.append(f"{p}: content type should be text/vnd.tiddlywiki")

    edges = {}
    for title, (fields, body, path) in found.items():
        if title.startswith("$:/"):
            continue
        if fields.get("mandarin-kind") == "vocabulary":
            lesson_ids = title_list(fields.get("mandarin-lessons", ""))
            if not lesson_ids:
                errors.append(f"{title}: missing mandarin-lessons membership")
            for lesson_id in lesson_ids:
                if f"Lesson Vocabulary/{lesson_id}" not in found:
                    errors.append(f"{title}: unknown vocabulary lesson {lesson_id!r}")
        dependencies = title_list(fields.get("mandarin-prerequisites", ""))
        edges[title] = dependencies
        for dep in dependencies:
            if dep == title:
                errors.append(f"{title}: self prerequisite")
            if dep not in found:
                errors.append(f"{title}: missing prerequisite {dep!r}")
        # Only check ordinary wiki links in content, not widget/filter internals.
        for raw in LINK_RE.findall(body):
            if raw.startswith("$:/") or raw.startswith("http"):
                continue
            dest = raw.rsplit("|", 1)[-1].strip()
            if dest and dest not in found:
                errors.append(f"{title}: broken wiki link to {dest!r}")

    for cycle in detect_cycles(edges):
        errors.append("Prerequisite cycle: " + " -> ".join(cycle))

    required_indexes = ("Home", "Course Map", "Grammar Index",
                        "Vocabulary Index", "Character Index",
                        "Reading Index", "Exercise Index", "Wuxia Index")
    for title in required_indexes:
        if title not in found:
            errors.append(f"Missing navigation tiddler {title!r}")

    return errors, dict(counts)


def main() -> int:
    errors, counts = validate()
    print("Tiddlers:", sum(counts.values()), "categories:", dict(sorted(counts.items())))
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        print(f"FAILED: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print("PASS: metadata, link targets, prerequisite references and DAG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
