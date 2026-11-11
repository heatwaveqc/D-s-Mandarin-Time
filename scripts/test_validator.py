import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).with_name("validate_wiki.py")
spec = importlib.util.spec_from_file_location("validate_wiki", MODULE)
wiki = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wiki)


class ValidatorTests(unittest.TestCase):
    def test_parse_header(self):
        fields, body = wiki.parse_tiddler("title: Test\nmandarin-kind: grammar\n\nHello")
        self.assertEqual(fields["title"], "Test")
        self.assertEqual(body, "Hello")

    def test_title_list_with_spaces(self):
        self.assertEqual(wiki.title_list("[[Grammar/SVO Word Order]] [[Lesson/01 First Sentences]]"),
                         ["Grammar/SVO Word Order", "Lesson/01 First Sentences"])

    def test_lexical_band_choices(self):
        self.assertEqual(wiki.VALID_LEXICAL_BANDS,
                         {"fundamental", "high-use", "high-availability", "wuxia-specialist"})

    def test_cycle_detection(self):
        self.assertEqual(wiki.detect_cycles({"A": ["B"], "B": ["A"]}),
                         [["A", "B", "A"]])

    def test_acyclic(self):
        self.assertEqual(wiki.detect_cycles({"A": ["B"], "B": []}), [])



class VocabularyLessonMembershipTests(unittest.TestCase):
    """A corpus entry does not have to be assigned to a course lesson."""

    @staticmethod
    def validate_sample(lesson_field="", indexed_lessons=()):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            indexes = ("Home", "Course Map", "Grammar Index",
                       "Vocabulary Index", "Character Index",
                       "Reading Index", "Exercise Index", "Wuxia Index")
            for n, title in enumerate(indexes):
                (root / f"nav-{n}.tid").write_text(
                    f"title: {title}\n"
                    "type: text/vnd.tiddlywiki\n"
                    "tags: [[Mandarin Navigation]]\n"
                    "mandarin-kind: navigation\n"
                    "mandarin-level: foundation\n\n"
                    "Navigation.\n",
                    encoding="utf-8",
                )
            for lesson_id in indexed_lessons:
                (root / f"lesson-{lesson_id}.tid").write_text(
                    f"title: Lesson Vocabulary/{lesson_id}\n"
                    "type: text/vnd.tiddlywiki\n"
                    "tags: [[Mandarin Navigation]]\n"
                    "mandarin-kind: navigation\n"
                    "mandarin-level: beginner\n\n"
                    "Lesson vocabulary index.\n",
                    encoding="utf-8",
                )
            (root / "word.tid").write_text(
                "title: Vocabulary/测试\n"
                "type: text/vnd.tiddlywiki\n"
                "tags: [[Mandarin Vocabulary]]\n"
                "mandarin-kind: vocabulary\n"
                "mandarin-level: reference\n"
                "mandarin-hanzi: 测试\n"
                "mandarin-pinyin: cèshì\n"
                "mandarin-gloss: test\n"
                "mandarin-pos: verb\n"
                + lesson_field + "\n"
                "测试。 — Cèshì. — Test.\n",
                encoding="utf-8",
            )
            return wiki.validate(root)

    def test_unassigned_word_is_valid(self):
        errors, counts = self.validate_sample()
        self.assertEqual(errors, [])
        self.assertEqual(counts["vocabulary"], 1)

    def test_word_assigned_to_existing_lesson_is_valid(self):
        errors, counts = self.validate_sample(
            "mandarin-lessons: L01\n", indexed_lessons=("L01",)
        )
        self.assertEqual(errors, [])
        self.assertEqual(counts["vocabulary"], 1)

    def test_word_assigned_to_missing_lesson_is_invalid(self):
        errors, _ = self.validate_sample("mandarin-lessons: L99\n")
        self.assertIn("Vocabulary/测试: unknown vocabulary lesson 'L99'", errors)


if __name__ == "__main__":
    unittest.main()
