from functools import reduce

class HTMLNode:
    def __init__(self, tag = None, value =None, children= None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        acc = ""
        if not self.props:
            return acc
        for prop in self.props:
            acc += f" {prop}=\"{self.props[prop]}\""
        return acc
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.props == other.props and self.children == other.children
