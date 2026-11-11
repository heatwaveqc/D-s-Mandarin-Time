import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).with_name("validate_lexicon.py")
spec = importlib.util.spec_from_file_location("validate_lexicon", MODULE)
lex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lex)


class LexicalInfrastructureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.words = self.root / "tiddlers" / "Vocabulary"
        self.words.mkdir(parents=True)
        self.research = self.root / "research"
        self.research.mkdir()
        self.sources = [
            {"id": "curriculum-editorial", "kind": "editorial",
             "source_url": "https://example.org/original", "license": "original",
             "accessed": "2026-11-11", "reuse_status": "editorial-original",
             "release": "1", "sha256": None},
            {"id": "wordfreq-zh", "kind": "frequency",
             "source_url": "https://example.org/wordfreq", "license": "CC BY-SA",
             "accessed": "2026-11-11", "reuse_status": "not-yet-approved",
             "release": None, "sha256": None}
        ]
        self.reg = [{"lexeme_id": "lx-000001",
                     "tiddler_path": "tiddlers/Vocabulary/test.tid",
                     "status": "active", "assigned_batch": "legacy", "notes": ""}]
        self.selection = []
        self.evidence = []
        self.write_word()
        self.save()

    def write_word(self, word_id="lx-000001", extras="", name="test.tid",
                   hanzi="测试", pinyin="cèshì"):
        if word_id is None:
            identity = ""
        else:
            identity = f"mandarin-lexeme-id: {word_id}\n"
        (self.words / name).write_text(
            f"title: Vocabulary/{hanzi}\n"
            "type: text/vnd.tiddlywiki\n"
            "tags: [[Mandarin Vocabulary]]\n"
            "mandarin-kind: vocabulary\n"
            "mandarin-level: reference\n"
            + identity
            + f"mandarin-hanzi: {hanzi}\n"
            + f"mandarin-pinyin: {pinyin}\n"
            + "mandarin-gloss: test\n"
            + "mandarin-pos: verb\n"
            + extras + "\n"
            "测试。 — Cèshì. — Test.\n",
            encoding="utf-8")

    def save(self):
        (self.research / "lexical-sources.json").write_text(
            json.dumps({"schema_version": 1, "sources": self.sources}), encoding="utf-8")
        for name, columns, rows in (
            ("lexeme-id-registry.csv", lex.REGISTRY_COLUMNS, self.reg),
            ("lexical-selection.csv", lex.SELECTION_COLUMNS, self.selection),
            ("lexical-evidence.csv", lex.EVIDENCE_COLUMNS, self.evidence),
        ):
            with (self.research / name).open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=columns)
                writer.writeheader()
                writer.writerows(rows)

    def issues(self):
        return lex.validate(self.root)[0]

    def make_planned(self):
        self.reg.append({"lexeme_id": "lx-000002", "tiddler_path": "",
                         "status": "planned", "assigned_batch": "survey-01", "notes": ""})
        self.selection.append({
            "lexeme_id": "lx-000002", "simplified": "新词",
            "traditional": "新詞", "pinyin": "xīncí", "pos": "noun",
            "gloss": "new word", "selection_band": "",
            "candidate_key": "survey:example", "review_status": "selected", "notes": ""})
        self.save()

    def test_valid_editorial_record_without_lessons_or_source_ids(self):
        errors, counts = lex.validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts["lexemes"], 1)
        self.assertEqual(counts["planned"], 0)

    def test_missing_lexeme_id(self):
        self.write_word(word_id=None)
        self.assertTrue(any("missing/invalid mandarin-lexeme-id" in e for e in self.issues()))

    def test_wrong_registry_path(self):
        self.reg[0]["tiddler_path"] = "tiddlers/Vocabulary/another.tid"
        self.save()
        self.assertTrue(any("registry points" in e for e in self.issues()))

    def test_duplicate_lexical_id(self):
        self.write_word(name="other.tid", hanzi="其他")
        self.assertTrue(any("duplicate lexeme ID" in e for e in self.issues()))

    def test_research_only_source_id_rejected(self):
        self.write_word(extras="mandarin-source-ids: curriculum-editorial\n")
        self.assertTrue(any("research-only field mandarin-source-ids" in e for e in self.issues()))

    def test_research_only_band_rejected(self):
        self.write_word(extras="mandarin-lexical-band: fundamental\n")
        self.assertTrue(any("research-only field mandarin-lexical-band" in e for e in self.issues()))

    def test_planned_without_tiddler_is_valid(self):
        self.make_planned()
        self.assertEqual(self.issues(), [])
        self.assertEqual(lex.validate(self.root)[1]["planned"], 1)

    def test_planned_without_selection_row_fails(self):
        self.make_planned()
        self.selection.clear()
        self.save()
        self.assertTrue(any("needs a selection-roster row" in e for e in self.issues()))

    def test_planned_tiddler_path_must_be_blank(self):
        self.make_planned()
        self.reg[1]["tiddler_path"] = "tiddlers/Vocabulary/new.tid"
        self.save()
        self.assertTrue(any("planned lx-000002 must have empty" in e for e in self.issues()))

    def test_selection_without_registered_id_fails(self):
        self.make_planned()
        self.reg.pop()
        self.save()
        self.assertTrue(any("not an active/planned registered ID" in e for e in self.issues()))

    def test_duplicate_selection_id_fails(self):
        self.make_planned()
        self.selection.append(dict(self.selection[0]))
        self.save()
        self.assertTrue(any("duplicate lexeme ID" in e for e in self.issues()))

    def test_unknown_evidence_source_fails(self):
        self.evidence.append({
            "evidence_id": "ev-1", "lexeme_id": "lx-000001",
            "source_id": "missing-source", "claim_type": "sense",
            "claim_value": "test", "review_status": "checked",
            "reviewed_by": "", "reviewed_on": "", "notes": ""})
        self.save()
        self.assertTrue(any("unknown source" in e for e in self.issues()))

    def test_unapproved_frequency_claim_fails(self):
        self.evidence.append({
            "evidence_id": "ev-2", "lexeme_id": "lx-000001",
            "source_id": "wordfreq-zh", "claim_type": "frequency",
            "claim_value": "123", "review_status": "verified",
            "reviewed_by": "auditor", "reviewed_on": "2026-11-11", "notes": ""})
        self.save()
        self.assertTrue(any("requires approved, frozen source" in e for e in self.issues()))

    def test_approved_frequency_claim_allowed_in_research(self):
        self.sources[1].update({"reuse_status": "redistribution-approved",
                                "release": "v1", "sha256": "a" * 64})
        self.evidence.append({
            "evidence_id": "ev-2", "lexeme_id": "lx-000001",
            "source_id": "wordfreq-zh", "claim_type": "frequency",
            "claim_value": "123", "review_status": "verified",
            "reviewed_by": "auditor", "reviewed_on": "2026-11-11",
            "notes": "Fictitious unit-test evidence."})
        self.save()
        self.assertEqual(self.issues(), [])

    def test_register_new_word_without_source_fields(self):
        import register_lexeme
        self.write_word(word_id=None, name="new.tid", hanzi="新词", pinyin="xīncí")
        new_id = register_lexeme.register(self.root, "tiddlers/Vocabulary/new.tid", "batch-03")
        self.assertEqual(new_id, "lx-000002")
        self.assertNotIn("mandarin-source-ids:", (self.words / "new.tid").read_text())
        self.assertEqual(self.issues(), [])

    def test_register_planned_word_preserves_id(self):
        import register_lexeme
        self.make_planned()
        self.write_word(word_id=None, name="new.tid", hanzi="新词", pinyin="xīncí")
        new_id = register_lexeme.register(
            self.root, "tiddlers/Vocabulary/new.tid", "publish-01", planned_id="lx-000002")
        self.assertEqual(new_id, "lx-000002")
        self.assertEqual(self.reg[0]["status"], "active")
        self.assertEqual(self.issues(), [])
        with (self.research / "lexeme-id-registry.csv").open(encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        self.assertEqual(rows[1]["status"], "active")
        self.assertTrue(rows[1]["notes"].startswith("published:"))

    def test_planned_publication_wrong_reading_rejected(self):
        import register_lexeme
        self.make_planned()
        self.write_word(word_id=None, name="new.tid", hanzi="新词", pinyin="xīncǐ")
        with self.assertRaises(ValueError):
            register_lexeme.register(self.root, "tiddlers/Vocabulary/new.tid",
                                     "batch-03", planned_id="lx-000002")

    def test_no_id_reuse_after_retirement(self):
        old = [dict(self.reg[0], status="retired", tiddler_path="")]
        self.assertTrue(any("cannot be reactivated" in e
                            for e in lex.check_history(old, self.reg)))

    def test_planned_to_active_requires_publication_note(self):
        old = [{"lexeme_id": "lx-000002", "status": "planned", "tiddler_path": "",
                "assigned_batch": "survey", "notes": ""}]
        after = [dict(old[0], status="active", tiddler_path="tiddlers/Vocabulary/new.tid")]
        self.assertTrue(any("published:" in e for e in lex.check_history(old, after)))
        after[0]["notes"] = "published: batch-03"
        self.assertEqual(lex.check_history(old, after), [])

    def test_sequential_allocation(self):
        after = self.reg + [{
            "lexeme_id": "lx-000003", "tiddler_path": "",
            "status": "planned", "assigned_batch": "survey", "notes": ""}]
        self.assertTrue(any("sequentially" in e for e in lex.check_history(self.reg, after)))

    def test_rename_requires_audit_note(self):
        after = [dict(self.reg[0], tiddler_path="tiddlers/Vocabulary/new-name.tid")]
        self.assertTrue(any("moved without" in e for e in lex.check_history(self.reg, after)))
        after[0]["notes"] = "moved: renamed after lexical review"
        self.assertEqual(lex.check_history(self.reg, after), [])


if __name__ == "__main__":
    unittest.main()
