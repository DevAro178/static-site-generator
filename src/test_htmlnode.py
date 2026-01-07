import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        result = node.props_to_html()
        self.assertEqual(
            result,
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(
            tag="p",
            props={"class": "text"}
        )
        result = node.props_to_html()
        self.assertEqual(result, ' class="text"')

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(tag="p")
        result = node.props_to_html()
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
