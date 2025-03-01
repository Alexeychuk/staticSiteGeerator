import unittest
from src.functions.split_nodes_delimiter import split_nodes_delimiter
from src.functions.textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ])

    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.NORMAL),
        ])

    def test_italic(self):
        node = TextNode("This is text with a *italic phrase* in the middle", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.NORMAL),
        ])

    def test_extract_italic_and_leave_bold(self):
        node = TextNode("This is **text** with an _italic_ word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(new_nodes,[
            TextNode("This is **text** with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ])

    def test_extract_bold_and_leave_italic(self):
        node = TextNode("This is **text** with an _italic_ word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes,[
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an _italic_ word", TextType.NORMAL),
        ])