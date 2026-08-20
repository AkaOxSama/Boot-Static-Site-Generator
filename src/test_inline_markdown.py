import unittest

from md_to_textnode import split_nodes_delimeter

from textnode import TextNode, TextType

class TestInLineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is a bit **awkward**", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a bit ", TextType.TEXT),
                TextNode("awkward", TextType.BOLD),
            ],
            new_nodes
        )
    def test_delim_italic(self):
        node = TextNode("This is a text with a _italic_ connotation", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" connotation", TextType.TEXT)
            ],
            new_nodes
        )

    def test_delim_code(self):
        node = TextNode("This contains a `code script`", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This contains a ", TextType.TEXT),
                TextNode("code script", TextType.CODE)
            ],
            new_nodes
        )

    def test_delim_multi_bold(self):
        node = TextNode("This text can be **very** large and **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This text can be ", TextType.TEXT),
                TextNode("very", TextType.BOLD),
                TextNode(" large and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD)
            ],
            new_nodes
        )

    def test_delim_multi_italic(self):
        node = TextNode("This test are driving me _mad_ but not really", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This test are driving me ", TextType.TEXT),
                TextNode("mad", TextType.ITALIC),
                TextNode(" but not really", TextType.TEXT)
            ],
            new_nodes
        )

    def test_delim_bold_multiword(self):
        node = TextNode("This phrase **contains** multiple **bold** characters", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This phrase ", TextType.TEXT),
                TextNode("contains", TextType.BOLD),
                TextNode(" multiple ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" characters", TextType.TEXT)
            ],
            new_nodes
        )

    def test_delim_italic_multiword(self):
        node = TextNode("Hello _cruel world_", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("Hello ", TextType.TEXT),
                TextNode("cruel world", TextType.ITALIC)
            ],
            new_nodes
        )
    def test_delim_no_text(self):
        node = TextNode("`just code`", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("just code", TextType.CODE)
            ],
            new_nodes
        )

    def test_delim_no_texttype_TEXT(self):
        node = TextNode("**nothing**", TextType.BOLD)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("**nothing**", TextType.BOLD)
            ],
            new_nodes
        )

    def test_delim_invalid_format(self):
        node = TextNode("_something is wrong", TextType.TEXT)
        
        with self.assertRaises(Exception) as context:
            split_nodes_delimeter([node], "_", TextType.ITALIC)

        self.assertEqual(
            str(context.exception),
            "invalid Markdown syntax, formatted section not closed"
        )
