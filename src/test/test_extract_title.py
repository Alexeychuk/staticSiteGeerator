import unittest

from src.functions.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = """# This is a title\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""

        expected_result = "This is a title"

        self.assertEqual(extract_title(markdown), expected_result)

    def test_extract_with_header_not_one(self):
        markdown = """## This is a title\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""

        self.assertRaises(Exception, extract_title,markdown)

    def test_extract_with_no_title(self):
        markdown = """This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""

        self.assertRaises(Exception, extract_title, markdown)
