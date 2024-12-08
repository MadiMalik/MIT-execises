import unittest
import calc

"""
Documentation:

Unit Tests for Calculator Module
---------------------------------

This script contains unit tests for the functions in the `calc` module.
Tests are written using the `unittest` framework to validate the correctness
of the add, subtract, multiply, and divide functions.

Run the tests:
    python test_calc.py
"""



""" Goal: is not to write as many test as posible but to make sure to write good tests
"""

""" unittist.TestCase -> gives us access different testing capabilities within that class"""
class TestCalc(unittest.TestCase):
    """ Naming convention of test_ is required so when we run this iy=t know which method represents tests"""
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        
        with self.assertRaises(ValueError):
            calc.divide(10, 0)



""" We need to run unittest as our main module and pass is test_calc.py"""

if __name__ == '__main__':
    unittest.main()