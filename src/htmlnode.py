class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return (
            f"HTMLNode("
            f"tag={self.tag}, "
            f"value={self.value}, "
            f"children={self.children}, "
            f"props={self.props}"
            f")"
        )
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        # If props is None or empty, return empty string
        if not self.props:
            return ""

        result = ""

        # Loop through each key-value pair in the props dictionary
        for key, value in self.props.items():
            result += f' {key}="{value}"'

        return result

        