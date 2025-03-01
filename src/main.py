import sys

from functions.extract_markdown import extract_markdown_images
from functions.copy_static_to_public import copy_static_to_public
from functions.generate_page import generate_page
from functions.textnode import TextNode, TextType
import os

from functions.generate_pages_recursive import generate_pages_recursive


def main():
    copy_static_to_public()
    basepath = "/"

    cli_args = sys.argv
    if len(cli_args) >= 2:
        basepath = sys.argv[1]
    print(basepath)
    copy_static_to_public()
    generate_pages_recursive(os.path.join(os.getcwd(), "content"), os.path.join(os.getcwd(), "template.html"), "docs", basepath)


if __name__ == "__main__":
    main()