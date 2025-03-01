import unittest

from src.functions.leafnode import LeafNode
from src.functions.text_to_html import text_node_to_html_node
from src.functions.textnode import TextNode, TextType


class TestTextToHtml(unittest.TestCase):
    def test_normal_text(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.NORMAL))
        self.assertEqual(node, LeafNode(None, "This is a text node"))

    def test_bold_text(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.BOLD))
        self.assertEqual(node, LeafNode("b", "This is a text node"))

    def test_italic_text(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.ITALIC))
        self.assertEqual(node, LeafNode("i", "This is a text node"))

    def test_code_text(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.CODE))
        self.assertEqual(node, LeafNode("code", "This is a text node"))

    def test_link_text(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.LINK, "https://www.boot.dev"))
        self.assertEqual(node, LeafNode("a", "This is a text node", {"href": "https://www.boot.dev"}))

    def test_img_text(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.IMG, "https://www.boot.dev"))
        self.assertEqual(node, LeafNode("img", "", {"src": "https://www.boot.dev", "alt": "This is a text node"}))

    def test_error_with_invalid_text_type(self):
        with self.assertRaises(Exception):
            text_node_to_html_node(TextNode("This is a text node", None))