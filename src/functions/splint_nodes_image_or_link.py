from .extract_markdown import extract_markdown_images, extract_markdown_links
from .textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    result_nodes = []
    for node in old_nodes:
        node_text = node.text
        links = extract_markdown_images(node_text)
        if len(links) == 0:
            result_nodes.append(node)
            continue

        remaining_text = node_text
        for link in links:

            link_raw = f"![{link[0]}]({link[1]})"
            link_start_index = remaining_text.find(link_raw)

            prev = remaining_text[:link_start_index]

            remaining_text = remaining_text[link_start_index + len(link_raw):]
            if len(prev) != 0:
                result_nodes.append(TextNode(prev, TextType.NORMAL))

            result_nodes.append(TextNode(link[0], TextType.IMG, link[1]))

        if len(remaining_text) != 0:
            result_nodes.append(TextNode(remaining_text, TextType.NORMAL))
    return result_nodes


def split_nodes_link(old_nodes):
    result_nodes = []
    for node in old_nodes:
        node_text = node.text
        links = extract_markdown_links(node_text)

        if len(links) == 0:
            result_nodes.append(node)
            continue

        remaining_text = node_text
        for link in links:

            link_raw = f"[{link[0]}]({link[1]})"
            link_start_index = remaining_text.find(link_raw)

            prev = remaining_text[:link_start_index]

            remaining_text = remaining_text[link_start_index + len(link_raw):]
            if len(prev) != 0:
                result_nodes.append(TextNode(prev, TextType.NORMAL))

            result_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

        if len(remaining_text) != 0:
            result_nodes.append(TextNode(remaining_text, TextType.NORMAL))
    return result_nodes