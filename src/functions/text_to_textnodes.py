import re

from .textnode import TextNode, TextType
from .splint_nodes_image_or_link import split_nodes_image, split_nodes_link
from .split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    iteration_res =  [TextNode(text, TextType.NORMAL)]
    iteration_res = split_nodes_delimiter(iteration_res, "**", TextType.BOLD)
    iteration_res = split_nodes_delimiter(iteration_res, "**", TextType.BOLD)
    iteration_res = split_nodes_delimiter(iteration_res, "_", TextType.ITALIC)
    iteration_res = split_nodes_delimiter(iteration_res, "_", TextType.ITALIC)
    iteration_res = split_nodes_delimiter(iteration_res, "`", TextType.CODE)

    # while any(re.search(r"\*\*|\_|\`", iteration_res_node.text) for iteration_res_node in iteration_res):
    #     iteration_res = split_nodes_delimiter(iteration_res, "**", TextType.BOLD)
    #     iteration_res = split_nodes_delimiter(iteration_res, "_", TextType.ITALIC)
    #     iteration_res = split_nodes_delimiter(iteration_res, "`", TextType.CODE)

    iteration_res = split_nodes_image(iteration_res)
    iteration_res = split_nodes_link(iteration_res)

    return iteration_res

