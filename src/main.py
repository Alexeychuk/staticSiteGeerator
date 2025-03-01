from functions.extract_markdown import extract_markdown_images
from functions.copy_static_to_public import copy_static_to_public
from functions.generate_page import generate_page
from functions.textnode import TextNode, TextType
import os

from functions.generate_pages_recursive import generate_pages_recursive


def main():
    copy_static_to_public()
    # generate_page(os.path.join(os.getcwd(), "content", "index.md"), os.path.join(os.getcwd(), "template.html"), "public")
    generate_pages_recursive(os.path.join(os.getcwd(), "content"), os.path.join(os.getcwd(), "template.html"), "public")

if __name__ == "__main__":
    main()