import unittest

from blocks_markdown import markdown_to_blocks

class TestBlocksMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiple_inline(self):
        md = """
This `code` contains instructions:

Do not open this text with admin privileges
Do not share the contents of this file without permission

-This is not a joke
-The world depends on it

Regards
        
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This `code` contains instructions:",
                "Do not open this text with admin privileges\nDo not share the contents of this file without permission",
                "-This is not a joke\n-The world depends on it",
                "Regards"
            ]
        )

    def test_markdown_to_blocks_whitespace(self):
        md = """
According to all known laws of aviation, there is no way a bee should be able to fly. 

 Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible. 
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "According to all known laws of aviation, there is no way a bee should be able to fly.",
                "Its wings are too small to get its fat little body off the ground.\nThe bee, of course, flies anyway because bees don't care what humans think is impossible."
            ]
        )