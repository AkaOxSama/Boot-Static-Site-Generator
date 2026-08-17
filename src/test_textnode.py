import unittest
from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()