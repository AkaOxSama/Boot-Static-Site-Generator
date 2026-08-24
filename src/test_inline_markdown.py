import unittest

from inline_markdow import (
    split_nodes_delimeter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link,
)

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

    # Test for functions to extract links or images from markdown text
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This link [link](https://localhost.8888) is very safe"
        )
        self.assertListEqual([("link", "https://localhost.8888")], matches)

    def test_extract_markdown_images_with_multiple_formats(self):
        matches = extract_markdown_images(
            "This text is very ![simple](https://i.imgur.com/QEHxooZ.mp4) but this can be very [difficult](https://www.cia.com)"
        )
        self.assertListEqual([("simple", "https://i.imgur.com/QEHxooZ.mp4")], matches)

    def test_extract_markdown_links_with_multiple_formats(self):
        matches = extract_markdown_links(
            "This text is very ![simple](https://i.imgur.com/QEHxooZ.mp4) but this can be very [difficult](https://www.cia.com)"
        )
        self.assertListEqual([("difficult", "https://www.cia.com")], matches)

    def test_extract_markdown_images_with_multiple_images(self):
        matches = extract_markdown_images(
            "This text contains two ![image1](https://i.imgur.com/dfbd34fc.png) ![image2](https://i.imgur.com/h34bdsn1dd.jpg) images"
        )
        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/dfbd34fc.png"),
                ("image2", "https://i.imgur.com/h34bdsn1dd.jpg")
            ],
            matches
        )

    def test_extract_markdown_links_with_multiple_links(self):
        matches = extract_markdown_links(
            "This text contains two [link1](https://www.darkweb.com) [link2](https://www.whiteweb.com) links"
        )
        self.assertListEqual(
            [
                ("link1", "https://www.darkweb.com"),
                ("link2", "https://www.whiteweb.com")
            ],
            matches
        )

    # Test for split nodes image and split nodes link

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://www.github.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.github.com"),
            ],
            new_nodes
        )

    def test_split_multiple_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes
        )

    def test_split_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )