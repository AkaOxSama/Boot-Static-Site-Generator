import unittest

from blocks_markdown import *

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

    
    # Test for Block Types
    def test_block_to_BlockType_heading(self):
        block = "# This is a heading"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.HEADING
        )
    
    def test_block_to_BlockType_heading_no_whitespace(self):
        block = "#This is a heading"
        
        with self.assertRaises(Exception) as context:
            block_to_block_type(block)

        self.assertEqual(
            str(context.exception),
            "invalid heading md syntax, missing ' ' after '#'"
        )

    def test_block_to_BlockType_heading_invalid_ch(self):
        block = "####### This heading has to many '#'"

        with self.assertRaises(Exception) as context:
            block_to_block_type(block)

        self.assertEqual(
            str(context.exception),
            "invalid heading md syntax, more than 6 '#' characters found"
        )

    def test_block_to_BlockType_code(self):
        block = "```\n This is real code.```"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.CODE
        )

    def test_block_to_BlockType_quote(self):
        block = ">'I am the Infinity War' - Ironman"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.QUOTE
        )

    def test_block_to_BlockType_unordered_list(self):
        block = "- This is a very unordered\n-List."
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.UNORDERED_LIST
        )

    def test_block_to_BlockType_ordered_list(self):
        block = "1. This list is ordered\n2. Like my room."
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.ORDERED_LIST
        )

    def test_block_to_BlockType_paragraph(self):
        block = "This is a normal paragraph\nWith nothing shady going on in it"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.PARAGRAPH
        )


    # Test functions for markdown_to_html_node function
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()