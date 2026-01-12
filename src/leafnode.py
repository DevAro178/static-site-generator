from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Leaf nodes cannot have children
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        # If tag is None, return raw text
        if self.tag is None:
            return self.value

        # Render HTML element
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (
            f"LeafNode("
            f"tag={self.tag}, "
            f"value={self.value}, "
            f"props={self.props}"
            f")"
        )
