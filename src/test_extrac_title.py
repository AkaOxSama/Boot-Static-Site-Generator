import unittest

from website_extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_single(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")
    def test_extract_title_multiple_headings(self):
        md = """
# This is the title.
## This is not the title
"""
        title = extract_title(md)
        self.assertEqual(title, "This is the title.")

    def test_extract_title_invalid(self):
        md = "## Is this a title?"

        with self.assertRaises(Exception) as context:
            extract_title(md)

        self.assertEqual(
            str(context.exception),
            "invalid markdown syntax, missing '# ' to extract a proper title"
        )