import re
from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import markdown_to_blocks

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

def text_to_children(text):
    from textnode import text_node_to_html_node, text_to_textnodes

    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        # -------- HEADING --------
        if block_type == BlockType.HEADING:
            level = block.count("#", 0, block.find(" "))
            text = block[level + 1 :]
            tag = f"h{level}"
            children.append(
                ParentNode(tag, text_to_children(text))
            )

        # -------- PARAGRAPH --------
        elif block_type == BlockType.PARAGRAPH:
            # collapse internal newlines into spaces
            paragraph_text = block.replace("\n", " ")
            children.append(
                ParentNode("p", text_to_children(paragraph_text))
            )

        # -------- CODE BLOCK --------
        elif block_type == BlockType.CODE:
            # remove opening and closing ```
            code_content = block[4:-3]
            code_node = LeafNode("code", code_content)
            children.append(
                ParentNode("pre", [code_node])
            )

        # -------- QUOTE --------
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            stripped = [line.lstrip(">").lstrip() for line in lines]
            quote_text = " ".join(stripped)
            children.append(
                ParentNode("blockquote", text_to_children(quote_text))
            )

        # -------- UNORDERED LIST --------
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                text = line[2:]
                items.append(
                    ParentNode("li", text_to_children(text))
                )
            children.append(
                ParentNode("ul", items)
            )

        # -------- ORDERED LIST --------
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                # remove "1. "
                text = line.split(". ", 1)[1]
                items.append(
                    ParentNode("li", text_to_children(text))
                )
            children.append(
                ParentNode("ol", items)
            )

    return ParentNode("div", children)
