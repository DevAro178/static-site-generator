import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(
            BlockType.HEADING,
            block_to_block_type("# Heading")
        )

    def test_heading_six_hashes(self):
        self.assertEqual(
            BlockType.HEADING,
            block_to_block_type("###### Small Heading")
        )

    def test_code_block(self):
        block = "```\ncode here\n```"
        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_not_code_block(self):
        block = "```\ncode here"
        self.assertNotEqual(BlockType.CODE, block_to_block_type(block))

    def test_quote_block(self):
        block = "> line one\n> line two"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))


    def test_quote_with_space(self):
        block = "> line one\n>line two"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))
        
    def test_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))


    def test_invalid_unordered_list(self):
        block = "- Item 1\nItem 2"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))


    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(block))


    def test_invalid_ordered_list_wrong_number(self):
        block = "1. Item 1\n3. Item 2"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))


    def test_invalid_ordered_list_not_starting_at_one(self):
        block = "2. Item 1\n3. Item 2"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_paragraph(self):
        block = "This is just a paragraph."
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))


       
if __name__ == "__main__":
    unittest.main()
