import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_default_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq_1(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        node = HTMLNode(
            "p", "this is a paragraph", [child1, child2], {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )

        node2 = HTMLNode(
            "p", "this is a paragraph", [child1, child2], {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )

        self.assertEqual(node, node2)

    def test_props_to_html_eq_1(self):
        node = HTMLNode()
        node2 = HTMLNode()

        self.assertEqual(str(node.props_to_html()), str(node2.props_to_html()))

    def test_props_to_html_eq_2(self):
        child = HTMLNode("p", "paragraph")
        node = HTMLNode("a", "test link", [child], {"href": "https://www.google.com",})
        node2 = HTMLNode("a", "test link", [child], {"href": "https://www.google.com",})

        self.assertEqual(str(node.props_to_html()), str(node2.props_to_html()))

    def test_not_eq_1(self):
        child = HTMLNode("P", "paragraph")
        child2 = HTMLNode(None, "paragraph")

        node = HTMLNode(None, None, [child])
        node2 = HTMLNode(None, None, [child2])

        self.assertNotEqual(node, node2)

    def test_noteq_2(self):
        node = HTMLNode("a", "text", None, {"href": "https://www.google.com",})
        node2 = HTMLNode("b", "text", None, {"href": "https://www.google.com",})

        self.assertNotEqual(node, node2)

    def test_not_eq_3(self):
        child1 = HTMLNode()
        child2 = HTMLNode()

        node = HTMLNode(
            "p", "this is a paragraph", [child1, child2], {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        node2 = HTMLNode()

        self.assertNotEqual(node, node2)

    def test_props_to_html_correct_transformation(self):
        node = HTMLNode(None, None, None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        prop = node.props_to_html()

        self.assertTrue(prop.startswith(" "))
        self.assertFalse(prop.endswith(" "))

if __name__ == "__main__":
    unittest.main()

        
