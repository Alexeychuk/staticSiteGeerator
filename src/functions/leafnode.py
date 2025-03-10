from .htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        props = ""
        if self.props:
            props = self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"