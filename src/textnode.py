from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
    
class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None, *args, **kwargs):
        self.text=TEXT
        self.text_type=TEXT_TYPE
        self.url=URL
        
    def __eq__(self,node):
        return (
                self.text == node.text and 
                self.text_type == node.text_type and 
                self.url == node.url
            )
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'