import unittest
import mystery_4

class TestMystery4(unittest.TestCase):
    """Unit tests for the mystery_4 function."""
    def test_positive_integer(self):
        """ Test positive integer """
        self.assertEqual(mystery_4.mystery_4(4), [0, 1, 2, 3])
        self.assertEqual(mystery_4.mystery_4(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_zero(self):
        """ Test with zero"""
        self.assertEqual(mystery_4.mystery_4(0), [])

    def test_negative_integer(self):
        """ Test with a negative inputs (should raise an error)"""
        with self.assertRaises(ValueError):
            mystery_4.mystery_4(-5)
    
    def test_non_integer(self):
        """ Test with non integer inputs """
        with self.assertRaises(TypeError):
            mystery_4.mystery_4("a")
        with self.assertRaises(TypeError):
            mystery_4.mystery_4(3.5) # will fail because we did not specify any error for the float nums



if __name__ == '__main__':
    unittest.main()
