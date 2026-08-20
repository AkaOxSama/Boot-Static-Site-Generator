import re
from textnode import *

def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    text_nodes_list = []

    def extract_between(text, char):
        parts = text.split(char)
        return parts[1::2]

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_nodes_list.append(node)
            continue

        if node.text.count(delimeter) % 2 != 0:
            raise Exception("invalid Markdown syntax, formatted section not closed")
        
        formatted_text = extract_between(node.text, delimeter)

        split_nodes = []
        sections = node.text.split(delimeter)
        for sect in range(len(sections)):
            if sections[sect] == "":
                continue
            if sections[sect] in formatted_text:
                split_nodes.append(TextNode(sections[sect], text_type))
            else:
                split_nodes.append(TextNode(sections[sect], TextType.TEXT))

        text_nodes_list.extend(split_nodes)

    return text_nodes_list

        
        
        