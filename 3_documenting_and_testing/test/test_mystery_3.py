import unittest
import mystery_3  # Importing the module containing the mystery_3 function

class TestMystery3(unittest.TestCase):
    """
    Unit tests for the function `mystery_3` in the `mystery_3` module.
    """

    def test_a_less_than_b(self):
        """Test if `a` is less than `b`."""
        self.assertEqual(mystery_3.mystery_3(3, 5), 3)
        self.assertEqual(mystery_3.mystery_3(-3, 0), -3)

    def test_a_greater_than_b(self):
        """ Test if a is greater than b"""
        self.assertEqual(mystery_3.mystery_3(7, 5), 5)
        self.assertEqual(mystery_3.mystery_3(10, -2), -2)

    def test_a_equal_to_b(self):
        """Test if both values are equal"""
        self.assertEqual(mystery_3.mystery_3(5, 5), 10)
        self.assertEqual(mystery_3.mystery_3(0, 0), 0)
    

if __name__ == '__main__':
    unittest.main()