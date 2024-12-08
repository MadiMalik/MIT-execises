import unittest 
from mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """ Unit tests for the mystery_2 function."""

    def test_empty_input(self):
        """Test with empty input """
        self.assertIsNone(mystery_2([])) # empty list
        self.assertIsNone(mystery_2("")) # empty str

    def test_non_emty_input(self):
        """Test with non empty input """
        self.assertEqual(mystery_2([1, 3, 6, 7]), 4) # list with 3 elements 
        self.assertEqual(mystery_2("Madiha"), 6) # str with 6 chars


    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(mystery_2([None]), 1)
        self.assertEqual(mystery_2([""]), 1)




if __name__ == "__main__":
    unittest.main()