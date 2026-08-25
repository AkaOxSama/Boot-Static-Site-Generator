from enum import Enum
from htmlnode import *
from textnode import *

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

