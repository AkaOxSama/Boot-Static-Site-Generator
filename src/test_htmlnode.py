import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    # HTMLNode Test:
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    # LeafNode Test:
    def test_leaf_to_html(self):
        node = LeafNode(None, "This is a very normal text.")
        self.assertEqual(node.to_html(), "This is a very normal text.")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_repr(self):
        node = LeafNode("a", "Search This!", {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "LeafNode(a, Search This!, {'href': 'https://www.google.com'})")

    # ParentNode Test:
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("a", "this is a child")
        child2 = LeafNode("p", "this is another child")
        parent = ParentNode("p", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            "<p><a>this is a child</a><p>this is another child</p></p>"
        )

    def test_to_html_with_children_with_props(self):
        child_node = LeafNode("a", "this is very bold of you", {"href": "www.youtube.com"})
        parent_node = ParentNode("p", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            '<p><a href="www.youtube.com">this is very bold of you</a></p>'
        )

    def test_leaf_to_html_ultra_nested(self):
        child1 = LeafNode("a", "link", {"href": "www.bootdev.com"})
        parent1 = ParentNode("b", [child1])
        parent2 = ParentNode("p", [parent1])
        parent3 = ParentNode("a", [parent2], {"href": "www.google.com"})

        self.assertEqual(
            parent3.to_html(),
            '<a href="www.google.com"><p><b><a href="www.bootdev.com">link</a></b></p></a>'
        )


if __name__ == "__main__":
    unittest.main()
