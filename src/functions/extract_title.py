from .markdown_to_blocks import markdown_to_blocks
import re

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    found_title = None

    for block in blocks:
        search = re.search('^#\s', block)
        if not search:
            continue
        found_title = re.sub('^#\s', '', block)
        break

    if found_title is None:
        raise Exception("No title found")

    return found_title