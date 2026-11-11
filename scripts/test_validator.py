import importlib.util
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

    def test_cycle_detection(self):
        self.assertEqual(wiki.detect_cycles({"A": ["B"], "B": ["A"]}),
                         [["A", "B", "A"]])

    def test_acyclic(self):
        self.assertEqual(wiki.detect_cycles({"A": ["B"], "B": []}), [])


if __name__ == "__main__":
    unittest.main()
