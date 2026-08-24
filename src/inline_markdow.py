import re
from textnode import *

# Function to split raw text into TextNodes with different TextType
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


# Function to split text nodes into a list of TextNodes for images
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

# Function to split text nodes into a list of TextNodes for links
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


# Function to extract images from markdown text
def extract_markdown_images(text: str) -> list[tuple["str", "str"]]:
    matches = re.findall(r"!\[(.*?)]\((.*?)\)", text)
    return matches

# Function to extract links from markdown text
def extract_markdown_links(text: str) -> list[tuple["str", "str"]]:
    matches = re.findall(r"(?<!!)\[(.*?)]\((.*?)\)", text)
    return matches


# Function that combines all the splitting functions into a single one
def text_to_textnodes(text: str) -> list[TextNode]:
    node = [TextNode(text, TextType.TEXT)]

    delimiters = [
        ("**", TextType.BOLD),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE),
    ]

    for delimiter, text_type in delimiters:
        node = split_nodes_delimeter(node, delimiter, text_type)

    node = split_nodes_image(node)
    node = split_nodes_link(node)

    return node