from .textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_nodes = []

    for node in old_nodes:
        if delimiter not in node.text:
            result_nodes.append(node)
            continue

        for i in range(len(node.text)):
            if node.text[i:i+len(delimiter)] == delimiter and node.text[i:i+len(delimiter)+1] != delimiter + delimiter:
                split_value = i + len(delimiter) - 1

                result_nodes.append(TextNode(node.text[:i], node.text_type))
                subtext = node.text[split_value + 1:]

                for j in range(len(subtext)):
                    if subtext[j:j+len(delimiter)] == delimiter:
                        split_value = j + len(delimiter) - 1
                        result_nodes.append(TextNode(subtext[:j], text_type))
                        result_nodes.append(TextNode(subtext[split_value + 1:], node.text_type))
                        break
                break

    return result_nodes