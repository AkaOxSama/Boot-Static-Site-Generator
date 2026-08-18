class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        html_format = ""
        for key, value in self.props.items():
            html_format += f" {key}={value}"

        return html_format

    def __repr__(self):
        representation = f"TAG: {self.tag}\n VALUE: {self.value}\n"
        representation += "CHILDREN LIST:\n"
        if self.children is not None:
            for child in self.children:
                representation += f"CHILD: {child}\n"
        else:
            representation += "0\n"
        representation += "PROPS\n"

        if self.props is not None:
            for key, value in self.props.items():
                representation += f"MK_TAG = {key}: HTML = {value}\n"
        else:
            representation += "0\n"

        return representation

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplementedError

        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )