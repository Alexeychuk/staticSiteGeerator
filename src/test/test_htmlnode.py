import unittest

from src.functions.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("h1", "Hello World", None, {"id": "hello-world", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " id=\"hello-world\" target=\"_blank\"")
    def test_to_html_execption(self):
        self.assertRaises(NotImplementedError, HTMLNode("h1", "Hello World", None, {"id": "hello-world", "target": "_blank"}).to_html)
    def test_print(self):
        node = HTMLNode("h1", "Hello World", None, {"id": "hello-world", "target": "_blank"})
        self.assertEqual(str(node), "HTMLNode(h1, Hello World, None, {'id': 'hello-world', 'target': '_blank'})")