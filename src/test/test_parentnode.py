import unittest

from src.functions.leafnode import LeafNode
from src.functions.parentnode import ParentNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_only_leaf_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_parent_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        main_node = ParentNode("div", [node])

        self.assertEqual(main_node.to_html(), "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")

    def test_to_html_with_deeply_nested_parent_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        second_node = ParentNode("div", [node])

        main_node = ParentNode("div", [second_node], {"class": "main-div"})

        self.assertEqual(main_node.to_html(), "<div class=\"main-div\"><div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div></div>")

    def test_error_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None).to_html()

    def test_error_with_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")]).to_html()