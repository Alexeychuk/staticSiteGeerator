from unittest import TestCase

from src.functions.htmlnode import HTMLNode
from src.functions.markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(TestCase):
    def test_markdown_to_html_unordered_list(self):
        markdown = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        expected_result = HTMLNode("div", None, [
            HTMLNode("ul", None, [
                HTMLNode("li",  None, [HTMLNode(None, "This is the first list item in a list block")]),
                HTMLNode("li",  None, [HTMLNode(None, "This is a list item")]),
                HTMLNode("li",  None, [HTMLNode(None, "This is another list item")]),
            ])
        ])


        self.maxDiff = None
        self.assertEqual(markdown_to_html_node(markdown), expected_result)
    def test_markdown_to_html_node(self):
        markdown = "## This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        expected_result = HTMLNode("div", None,  [
            HTMLNode("h2", None, [HTMLNode(None,"This is a heading")]),
            HTMLNode("p", None,
                     [HTMLNode(None, "This is a paragraph of text. It has some "),
                      HTMLNode("b", "bold"),
                      HTMLNode(None, " and "),
                      HTMLNode("i", "italic"),
                      HTMLNode(None, " words inside of it.")]),
            HTMLNode("ul", None, [
                HTMLNode("li",  None, [HTMLNode(None, "This is the first list item in a list block")]),
                HTMLNode("li",  None, [HTMLNode(None, "This is a list item")]),
                HTMLNode("li",  None, [HTMLNode(None, "This is another list item")]),
            ])
        ])
        self.maxDiff = None
        self.assertEqual(markdown_to_html_node(markdown), expected_result)

    def test_ordered_list(self):
        markdown = """1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn"""

        expected_result = HTMLNode("div", None, [
            HTMLNode("ol", None, [
                HTMLNode("li",  None, [HTMLNode(None, "Gandalf")]),
                HTMLNode("li",  None, [HTMLNode(None, "Bilbo")]),
                HTMLNode("li",  None, [HTMLNode(None, "Sam")]),
                HTMLNode("li",  None, [HTMLNode(None, "Glorfindel")]),
                HTMLNode("li",  None, [HTMLNode(None, "Galadriel")]),
                HTMLNode("li",  None, [HTMLNode(None, "Elrond")]),
                HTMLNode("li",  None, [HTMLNode(None, "Thorin")]),
                HTMLNode("li",  None, [HTMLNode(None, "Sauron")]),
                HTMLNode("li",  None, [HTMLNode(None, "Aragorn")]),
            ])
        ])
        self.maxDiff = None
        self.assertEqual(markdown_to_html_node(markdown), expected_result)


    def test_markdown_to_html_code(self):
        markdown = "```This is a code block\nsecond row of it\nthird row```"
        print(markdown_to_html_node(markdown))
        expected_result = HTMLNode("div", None,  [
            HTMLNode("pre", None, [HTMLNode("code", "This is a code block\nsecond row of it\nthird row")])
        ])
        self.maxDiff = None
        self.assertEqual(markdown_to_html_node(markdown), expected_result)

    def test_markdown_to_html_paragraph(self):
        markdown = "This is a paragraph\n\n This is a paragraph of text. It has some **bold** and _italic_ words inside of it."

        expected_result = HTMLNode("div", None, [
            HTMLNode("p", None, [HTMLNode(None, "This is a paragraph")]),
            HTMLNode("p", None,
                     [HTMLNode(None, "This is a paragraph of text. It has some "),
                      HTMLNode("b", "bold"),
                      HTMLNode(None, " and "),
                      HTMLNode("i", "italic"),
                      HTMLNode(None, " words inside of it.")])
        ])

        self.assertEqual(markdown_to_html_node(markdown), expected_result)

    def test_markdown_to_html_with_link(self):
        markdown = "This is a paragraph\n\nThis is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        expected_result = HTMLNode("div", None, [
            HTMLNode("p", None, [HTMLNode(None, "This is a paragraph")]),
            HTMLNode("p", None,
                     [HTMLNode(None, "This is text with a link "),
                      HTMLNode("a", "to boot dev", None, {"href": "https://www.boot.dev"}),
                      HTMLNode(None, " and "),
                      HTMLNode("a", "to youtube", None, {"href": "https://www.youtube.com/@bootdotdev"})
                      ])])

        self.assertEqual(markdown_to_html_node(markdown), expected_result)

    def test_markdown_to_html_with_img(self):
        markdown = "This is a paragraph\n\nThis is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        expected_result = HTMLNode("div", None, [
            HTMLNode("p", None, [HTMLNode(None, "This is a paragraph")]),
            HTMLNode("p", None,
                     [HTMLNode(None, "This is text with a "),
                      HTMLNode("img", "image", None, {"src": "https://i.imgur.com/aKaOqIh.gif", "alt": "rick roll"}),
                      HTMLNode(None, " and "),
                      HTMLNode("img", "image", None, {"src": "https://i.imgur.com/fJRm4Vk.jpeg", "alt": "obi wan"})
                      ])])
        self.maxDiff = None
        self.assertEqual(markdown_to_html_node(markdown), expected_result)