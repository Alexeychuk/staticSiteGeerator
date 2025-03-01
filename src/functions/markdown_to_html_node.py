from .block_to_block_type import block_to_block_type
from .leafnode import LeafNode
from .parentnode import ParentNode
from .markdown_to_blocks import markdown_to_blocks
from .text_to_textnodes import text_to_textnodes
from .textnode import TextType

import re

# Loop over each block:
# Determine the type of block (you already have a function for this)
# Based on the type of block, create a new HTMLNode with the proper data
# Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text)
# function that works for all block types. It takes a string of text and returns a list of HTMLNodes that
# represent the inline markdown using previously created functions (think TextNode -> HTMLNode).

block_type_to_tag = {
    "quote":"blockquote",
    "paragraph":"p",
}

block_type_to_parent_child_tag = {
    "code":{
        "parent_tag": "pre",
        "child_tag": "code",
        "pattern": "```",
    },
}

block_type_to_parent_and_iterated_child_tag = {
    "unordered_list":{
        "parent_tag": "ul",
        "child_tag": "li",
        "pattern": r"^[*-]\s.+",
        "remove_prefix": r"[*-]\s"
    },
    "ordered_list":{
        "parent_tag": "ol",
        "child_tag": "li",
        "pattern": r"^[\d]\.\s.+",
        "remove_prefix": r"^[\d]\.\s"
    },
}

inline_tags_to_text_nodes_types = {
     TextType.BOLD: "b"
    ,TextType.ITALIC: "i"
    ,TextType.CODE: "code"
    ,TextType.LINK: "a"
    ,TextType.IMG: "img"
}

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    result = []
    for textNode in textnodes:
        if len(textNode.text) == 0:
            continue
        if textNode.text_type == TextType.IMG:
            result.append(LeafNode(inline_tags_to_text_nodes_types[textNode.text_type], "image",  {"src": textNode.url, "alt": textNode.text}))
            continue
        if textNode.text_type == TextType.LINK:
            result.append(LeafNode(inline_tags_to_text_nodes_types[textNode.text_type], textNode.text,  {"href": textNode.url}))
            continue
        if textNode.text_type == TextType.NORMAL:
            result.append(LeafNode(None, textNode.text))
            continue
        result.append(LeafNode(inline_tags_to_text_nodes_types[textNode.text_type], textNode.text))
    return result

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "quote":
            children = text_to_children(block.lstrip("> ").replace("> ", " ").replace(">", " ").replace("\n", ""))
            nodes.append(ParentNode(block_type_to_tag[block_type], children))
            continue
        elif block_type in block_type_to_tag:
            children = text_to_children(block)
            nodes.append(ParentNode(block_type_to_tag[block_type], children))

        elif block_type in block_type_to_parent_child_tag:
            if block.replace("```", "").strip() == "":
                print("Empty code block")
                continue
            child = LeafNode(block_type_to_parent_child_tag[block_type]["child_tag"], block.replace("```", "").strip())
            nodes.append(ParentNode(block_type_to_parent_child_tag[block_type]["parent_tag"],  [child]))

        elif block_type in block_type_to_parent_and_iterated_child_tag:
            splited_items = list(map(lambda item: re.sub(block_type_to_parent_and_iterated_child_tag[block_type]["remove_prefix"], "", item),re.findall(block_type_to_parent_and_iterated_child_tag[block_type]["pattern"], block, re.MULTILINE)))

            def to_li(text):
                return ParentNode("li",  text_to_children(text.replace("\n", "")))

            children = list(map(to_li, splited_items))
            nodes.append(ParentNode(block_type_to_parent_and_iterated_child_tag[block_type]["parent_tag"],  children))

        elif block_type == "heading":
            header_number = re.search('^#{1,6}', block).group()
            text_value = re.sub('^#{1,6}\s', '', block)

            nodes.append(ParentNode(f"h{len(header_number)}", text_to_children(text_value)))

    return ParentNode("div", nodes)