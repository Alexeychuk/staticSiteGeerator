import unittest
from src.functions.splint_nodes_image_or_link import split_nodes_image, split_nodes_link
from src.functions.textnode import TextNode, TextType


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_link_nodes(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        expected =   [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]

        self.assertEqual(split_nodes_link([node]), expected)

    def test_extract_link_nodes_with_link_at_start(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        expected =   [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]

        self.assertEqual(split_nodes_link([node]), expected)

    def test_extract_link_nodes_with_link_at_end(self):
        node = TextNode(
            "and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        expected =   [
            TextNode("and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]

        self.assertEqual(split_nodes_link([node]), expected)
    def test_extract_link_no_extraction(self):
        node = TextNode(
            "This is text with a link",
            TextType.NORMAL,
        )
        expected =   [
            TextNode(
                "This is text with a link",
                TextType.NORMAL,
            )
        ]

        self.assertEqual(split_nodes_link([node]), expected)

    def test_extract_image_nodes(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL,
        )
        expected =   [
        TextNode("This is text with a ", TextType.NORMAL),
        TextNode("rick roll", TextType.IMG, "https://i.imgur.com/aKaOqIh.gif"),
        TextNode(" and ", TextType.NORMAL),
        TextNode(
            "obi wan", TextType.IMG, "https://i.imgur.com/fJRm4Vk.jpeg"
        ),
    ]

        self.assertEqual(split_nodes_image([node]), expected)

