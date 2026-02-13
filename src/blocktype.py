import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
    


def block_to_block_type(block):
    lines = block.split("\n")

    # --- CODE BLOCK ---
    if (
        block.startswith("```")
        and block.endswith("```")
        and len(lines) >= 2
    ):
        return BlockType.CODE

    # --- HEADING ---
    if re.match(r"^#{1,6} .+", block):
        return BlockType.HEADING

    # --- QUOTE ---
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # --- UNORDERED LIST ---
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # --- ORDERED LIST ---
    is_ordered = True
    for i, line in enumerate(lines):
        if not re.match(rf"^{i+1}\. .+", line):
            is_ordered = False
            break

    if is_ordered:
        return BlockType.ORDERED_LIST

    # --- DEFAULT ---
    return BlockType.PARAGRAPH
