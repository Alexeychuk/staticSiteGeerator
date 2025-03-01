import re

def block_to_block_type(block):
    block_types = {
        "heading":["(^\#{1,6}\s.+)", re.MULTILINE],
        "code":["```(?:.|\n)*?```", re.MULTILINE],
        "quote":["^(>.*(?:\n|$))+", re.MULTILINE],
        "unordered_list":["^((\*|-) .*(\r?\n(\*|-) .*)*)$", re.MULTILINE],
        "ordered_list":["^(?:\d+\.\s+[A-Za-z]+(?:\n|$))+$", re.MULTILINE],
    }


    defined_type = "paragraph"

    for block_type in block_types:
            match = re.fullmatch(block_types[block_type][0], block, re.MULTILINE)
            if match:
                defined_type = block_type

                break

    return defined_type