
# Standard HTML Node class
class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        html_format = ""
        for key, value in self.props.items():
            html_format += f' {key}="{value}"'

        return html_format

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

# Leaf Node class to handle html lines with no children
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return self.value

        prop = self.props_to_html()

        return f"<{self.tag}{prop}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

# Parent Node Class to handle nesting HTML nodes inside one another
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("No tag found")

        if self.children is None:
            raise ValueError("No children found")

        html_string = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html_string += child.to_html()

        html_string += f"</{self.tag}>"

        return html_string

