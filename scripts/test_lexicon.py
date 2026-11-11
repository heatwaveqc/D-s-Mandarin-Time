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
            {
                "id": "curriculum-editorial", "kind": "editorial",
                "source_url": "https://example.org/editorial", "license": "original",
                "accessed": "2026-11-11", "reuse_status": "editorial-original",
                "release": "1", "sha256": None
            },
            {
                "id": "wordfreq-zh", "kind": "frequency",
                "source_url": "https://example.org/wordfreq", "license": "CC BY-SA",
                "accessed": "2026-11-11", "reuse_status": "not-yet-approved",
                "release": None, "sha256": None
            }
        ]
        self.reg = [{
            "lexeme_id": "lx-000001", "tiddler_path": "tiddlers/Vocabulary/test.tid",
            "status": "active", "assigned_batch": "test", "notes": ""
        }]
        self.evidence = []
        self.write_word()
        self.save()

    def write_word(self, word_id="lx-000001", sources="curriculum-editorial", extras=""):
        (self.words / "test.tid").write_text(
            "title: Vocabulary/测试\n"
            "type: text/vnd.tiddlywiki\n"
            "tags: [[Mandarin Vocabulary]]\n"
            "mandarin-kind: vocabulary\n"
            "mandarin-level: reference\n"
            f"mandarin-lexeme-id: {word_id}\n"
            f"mandarin-source-ids: {sources}\n"
            "mandarin-hanzi: 测试\n"
            "mandarin-pinyin: cèshì\n"
            "mandarin-gloss: test\n"
            "mandarin-pos: verb\n"
            + extras + "\n"
            "测试。 — Cèshì. — Test.\n",
            encoding="utf-8",
        )

    def save(self):
        (self.research / "lexical-sources.json").write_text(
            json.dumps({"schema_version": 1, "sources": self.sources}), encoding="utf-8"
        )
        for filename, columns, rows in (
            ("lexeme-id-registry.csv", lex.REGISTRY_COLUMNS, self.reg),
            ("lexical-evidence.csv", lex.EVIDENCE_COLUMNS, self.evidence),
        ):
            with (self.research / filename).open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=columns)
                writer.writeheader()
                writer.writerows(rows)

    def issues(self):
        return lex.validate(self.root)[0]

    def test_valid_editorial_record_without_lesson(self):
        errors, counts = lex.validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts["lexemes"], 1)

    def test_missing_lexeme_id(self):
        self.write_word(word_id="")
        self.assertTrue(any("missing/invalid mandarin-lexeme-id" in e for e in self.issues()))

    def test_wrong_registry_path(self):
        self.reg[0]["tiddler_path"] = "tiddlers/Vocabulary/another.tid"
        self.save()
        self.assertTrue(any("registry points" in e for e in self.issues()))

    def test_unknown_source(self):
        self.write_word(sources="made-up-source")
        self.assertTrue(any("unknown source ID" in e for e in self.issues()))

    def test_duplicate_lexical_id(self):
        (self.words / "other.tid").write_text(
            (self.words / "test.tid").read_text(encoding="utf-8").replace(
                "title: Vocabulary/测试", "title: Vocabulary/其他"
            ), encoding="utf-8"
        )
        self.assertTrue(any("duplicate lexeme ID" in e for e in self.issues()))

    def test_band_claim_requires_evidence(self):
        self.write_word(extras="mandarin-lexical-band: fundamental\n")
        self.assertTrue(any("mandarin-band-evidence-id" in e for e in self.issues()))

    def test_verified_band_evidence(self):
        self.evidence.append({
            "evidence_id": "ev-1", "lexeme_id": "lx-000001",
            "source_id": "curriculum-editorial", "claim_type": "band",
            "claim_value": "fundamental", "review_status": "verified",
            "reviewed_by": "editorial-auditor", "reviewed_on": "2026-11-11",
            "notes": "Demonstration only, not evidence of measured frequency"
        })
        self.save()
        self.write_word(extras="mandarin-lexical-band: fundamental\nmandarin-band-evidence-id: ev-1\n")
        self.assertEqual(self.issues(), [])

    def test_unverified_band_evidence_rejected(self):
        self.evidence.append({
            "evidence_id": "ev-1", "lexeme_id": "lx-000001",
            "source_id": "curriculum-editorial", "claim_type": "band",
            "claim_value": "fundamental", "review_status": "candidate",
            "reviewed_by": "", "reviewed_on": "", "notes": ""
        })
        self.save()
        self.write_word(extras="mandarin-lexical-band: fundamental\nmandarin-band-evidence-id: ev-1\n")
        self.assertTrue(any("must reference verified" in e for e in self.issues()))

    def test_unapproved_frequency_data_rejected(self):
        self.evidence.append({
            "evidence_id": "ev-2", "lexeme_id": "lx-000001",
            "source_id": "wordfreq-zh", "claim_type": "frequency",
            "claim_value": "123", "review_status": "verified",
            "reviewed_by": "editorial-auditor", "reviewed_on": "2026-11-11", "notes": ""
        })
        self.save()
        self.write_word(extras="mandarin-frequency-rank: 123\nmandarin-frequency-evidence-id: ev-2\n")
        self.assertTrue(any("requires approved, frozen source" in e for e in self.issues()))

    def test_approved_frequency_claim(self):
        self.sources[1].update({"reuse_status": "redistribution-approved",
                                "release": "v1", "sha256": "a" * 64})
        self.evidence.append({
            "evidence_id": "ev-2", "lexeme_id": "lx-000001",
            "source_id": "wordfreq-zh", "claim_type": "frequency",
            "claim_value": "123", "review_status": "verified",
            "reviewed_by": "editorial-auditor", "reviewed_on": "2026-11-11",
            "notes": "Fictitious unit-test example only"
        })
        self.save()
        self.write_word(extras="mandarin-frequency-rank: 123\nmandarin-frequency-evidence-id: ev-2\n")
        self.assertEqual(self.issues(), [])

    def test_sequential_allocation(self):
        after = self.reg + [{
            "lexeme_id": "lx-000003", "tiddler_path": "tiddlers/Vocabulary/other.tid",
            "status": "active", "assigned_batch": "next", "notes": ""
        }]
        self.assertTrue(any("sequentially" in e for e in lex.check_history(self.reg, after)))

    def test_no_id_reuse_after_retirement(self):
        old = [dict(self.reg[0], status="retired", tiddler_path="")]
        self.assertTrue(any("cannot be reactivated" in e for e in lex.check_history(old, self.reg)))

    def test_rename_requires_note(self):
        after = [dict(self.reg[0], tiddler_path="tiddlers/Vocabulary/new-name.tid")]
        self.assertTrue(any("moved without" in e for e in lex.check_history(self.reg, after)))
        after[0]["notes"] = "moved: renamed file during lexical reanalysis"
        self.assertEqual(lex.check_history(self.reg, after), [])


    def new_unregistered_word(self):
        original = (self.words / "test.tid").read_text(encoding="utf-8")
        original = original.replace("title: Vocabulary/测试", "title: Vocabulary/新词")
        original = original.replace("mandarin-lexeme-id: lx-000001\n", "")
        original = original.replace("mandarin-source-ids: curriculum-editorial\n", "")
        (self.words / "new.tid").write_text(original, encoding="utf-8")

    def test_register_lexeme_allocates_and_preserves_existing(self):
        import register_lexeme
        self.new_unregistered_word()
        new_id = register_lexeme.register(self.root, "tiddlers/Vocabulary/new.tid", "batch-03")
        self.assertEqual(new_id, "lx-000002")
        self.assertIn("mandarin-lexeme-id: lx-000002",
                      (self.words / "new.tid").read_text(encoding="utf-8"))
        self.assertEqual(self.issues(), [])
        self.assertTrue(any(r["lexeme_id"] == "lx-000002"
                            and r["assigned_batch"] == "batch-03"
                            for r in self._read_registry()))

    def _read_registry(self):
        with (self.research / "lexeme-id-registry.csv").open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))

    def test_register_lexeme_rejects_duplicate(self):
        import register_lexeme
        with self.assertRaises(ValueError):
            register_lexeme.register(self.root, "tiddlers/Vocabulary/test.tid", "batch-03")

    def test_register_lexeme_dry_run(self):
        import register_lexeme
        self.new_unregistered_word()
        result = register_lexeme.register(self.root, "tiddlers/Vocabulary/new.tid",
                                          "batch-03", dry_run=True)
        self.assertEqual(result, "lx-000002")
        self.assertEqual(len(self._read_registry()), 1)
        self.assertNotIn("mandarin-lexeme-id:",
                         (self.words / "new.tid").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
