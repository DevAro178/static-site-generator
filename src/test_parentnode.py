import unittest
from parentnode import ParentNode
from leafnode import LeafNode

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
    
def test_parent_with_empty_children(self):
    node = ParentNode("div", [])
    self.assertEqual(node.to_html(), "<div></div>")

def test_parent_multiple_children(self):
    node = ParentNode(
        "p",
        [
            LeafNode(None, "Hello "),
            LeafNode("b", "world"),
        ],
    )
    self.assertEqual(node.to_html(), "<p>Hello <b>world</b></p>")

def test_parent_missing_tag(self):
    node = ParentNode(None, [])
    with self.assertRaises(ValueError):
        node.to_html()

def test_parent_missing_children(self):
    node = ParentNode("div", None)
    with self.assertRaises(ValueError):
        node.to_html()

