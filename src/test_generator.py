import unittest
from generator import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_simple_title(self):
        self.assertEqual(
            extract_title("# Hello"),
            "Hello"
        )

    def test_title_with_whitespace(self):
        self.assertEqual(
            extract_title("#   Hello World   "),
            "Hello World"
        )

    def test_ignores_h2(self):
        with self.assertRaises(Exception):
            extract_title("## Not an h1")

    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("No heading here")
