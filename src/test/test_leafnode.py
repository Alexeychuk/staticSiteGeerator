import unittest

from src.functions.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>", "LeafNode should be able to create a paragraph")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>", "LeafNode should be able to create a link")

    def test_raw_value(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.", "LeafNode should be able to create a raw text")