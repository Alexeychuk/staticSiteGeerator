import unittest

from src.functions.block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_heading(self):
        block = "# This is a heading"

        expected_result = "heading"

        self.assertEqual(block_to_block_type(block), expected_result)

    def test_block_to_code(self):
        block = """```This is a code block
        Multiline, of course
        should work```"""

        expected_result = "code"

        self.assertEqual(block_to_block_type(block), expected_result)

    def test_block_to_quote(self):
        block = """>This is a quote block
>Multiline, of course
>should work"""

        expected_result = "quote"

        self.assertEqual(block_to_block_type(block), expected_result)

    def test_block_to_unordered_list(self):
        block = """* This is a quote block
* Multiline, of course
* should work"""
        expected_result = "unordered_list"

        self.assertEqual(block_to_block_type(block), expected_result)

    def test_block_to_unordered_list_with_dash(self):
        block = """- This is a quote block
- Multiline, of course
- should work"""
        expected_result = "unordered_list"

        self.assertEqual(block_to_block_type(block), expected_result)


    def test_block_to_ordered_list(self):
        block = """1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn"""
        expected_result = "ordered_list"

        self.assertEqual(block_to_block_type(block), expected_result)

    def test_block_to_broken_ordered_list(self):
        block = """1. This is a quote block
1. Multiline, of course
3. should work"""
        expected_result = "paragraph"

        self.assertEqual(block_to_block_type(block), expected_result)
    def test_block_to_paragraph(self):
        block = """This is paragraph
        multilined
        should be"""
        expected_result = "paragraph"

        self.assertEqual(block_to_block_type(block), expected_result)