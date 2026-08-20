import unittest
from textnode import *
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://localhost:8888")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://localhost:8888")
        self.assertEqual(node, node2)

    def test_noteq_1(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.bootdev.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "www.bootdev.com")
        self.assertNotEqual(node, node2)

    def test_noteq_2(self):
        node = TextNode("This is a normal text", TextType.TEXT)
        node2 = TextNode("This is a normal text", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is one text", TextType.TEXT, "www.google.es")
        node2 = TextNode("This is one text", TextType.TEXT, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_eq_4(self):
        node = TextNode("Code text", TextType.CODE, "www.youtube.com")
        node2 = TextNode("Image text", TextType.IMAGE, "www.artstation.com")
        self.assertNotEqual(node, node2)

    # Test textnode to htmlnode
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("this is very bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is very bold")

    def test_link(self):
        node = TextNode("this is a fishy link", TextType.LINK, "www.goggle.ia")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "this is a fishy link")
        self.assertEqual(html_node.props, {"href": "www.goggle.ia"})

if __name__ == "__main__":
    unittest.main()