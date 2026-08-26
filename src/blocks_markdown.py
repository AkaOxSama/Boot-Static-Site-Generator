from enum import Enum

from htmlnode import *
from textnode import *
from inline_markdow import *

# Divide md text file into blocks
def markdown_to_blocks(markdown:str) -> list[str]:
    return [line.strip() for line in markdown.split("\n\n") if line != ""]


# Enum for types of blocks in a md file
class BlockType(Enum):
    PARAGRAPH = "pg"
    HEADING = "hd"
    CODE = "c"
    QUOTE = "q"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"

def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#"):
        if block[1] == " ":
            return BlockType.HEADING
        
        i = 0
        ch = block[i]

        while ch == "#":
            i += 1
            ch = block[i]
        if i - 1 == 6:
            raise ValueError("invalid heading md syntax, more than 6 '#' characters found")
        if ch != " ":
            raise ValueError("invalid heading md syntax, missing ' ' after '#'")
        
        return BlockType.HEADING
            

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        return BlockType.QUOTE
    
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    
    if block.startswith(tuple(f"{n}." for n in range(1, 10))):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


# Function to convert full markdown documents into a single parent HTMLNode
def markdown_to_html_node(markdown: str) -> ParentNode:
    clean_blocks = markdown_to_blocks(markdown)
    child_parent_nodes = []

    for block in clean_blocks:
        b_type = block_to_block_type(block)

        match b_type:
            case BlockType.HEADING:
                child_parent_nodes.append(block_to_html_syntax(block, BlockType.HEADING))
            case BlockType.QUOTE:
                child_parent_nodes.append(block_to_html_syntax(block, BlockType.QUOTE))
            case BlockType.UNORDERED_LIST:
                child_parent_nodes.append(block_to_html_syntax(block, BlockType.UNORDERED_LIST))
            case BlockType.ORDERED_LIST:
                child_parent_nodes.append(block_to_html_syntax(block, BlockType.ORDERED_LIST))
            case BlockType.CODE:
                child_parent_nodes.append(block_to_html_syntax(block, BlockType.CODE))
            case BlockType.PARAGRAPH:
                child_parent_nodes.append(block_to_html_syntax(block, BlockType.PARAGRAPH))

    return ParentNode("div", child_parent_nodes)

# Helper function for blocktypes
def block_to_html_syntax(block: str, block_type: BlockType) -> ParentNode:
    match block_type:
        case BlockType.HEADING:
            i = 0
            while block[i] == "#":
                i += 1

            text = block[i + 1:]
            children = text_to_children(text)
            return ParentNode(f"h{i}", children)
        
        case BlockType.QUOTE:
            text = block[2:] if block[1] == " " else block[1:]
            children = text_to_children(text)
            return ParentNode(f"blockquote", children)

        case BlockType.UNORDERED_LIST:
            list_of_text = [lst for lst in block.split("\n") if lst != ""]
            text = ""
            for txt in list_of_text:
                text += f"<li>{txt}</li>"

            children = text_to_children(text)
            return ParentNode("ul", children)

        case BlockType.ORDERED_LIST:
            list_of_text = [lst for lst in block.split("\n") if lst != ""]
            text = ""
            for txt in list_of_text:
                text += f"<li>{txt}</li>"
            
            children = text_to_children(text)
            return ParentNode("ol", children)

        case BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            children = text_to_children(text)
            return ParentNode("p", children)

        case BlockType.CODE:
            text = block.strip("\n").strip("```").strip("\n")
            node = TextNode(text, TextType.CODE)
            child = text_node_to_html_node(node)
            return ParentNode("pre", [child])
            
# Helper function to convert text into a list of LeafNodes
def text_to_children(text: str) -> list[LeafNode]:
    children = []
    node = text_to_textnodes(text)
    for n in node:
        children.append(text_node_to_html_node(n))

    return children



