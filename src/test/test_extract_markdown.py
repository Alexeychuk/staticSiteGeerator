import unittest

from src.functions.htmlnode import HTMLNode
from src.functions.extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.assertEqual(extract_markdown_images(text), expected_result)

    def test_no_extraction(self):
        text = "This is text"
        expected_result = []

        self.assertEqual(extract_markdown_links(text), expected_result)

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        self.assertEqual(extract_markdown_links(text), expected_result)

