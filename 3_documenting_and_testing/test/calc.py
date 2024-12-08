"""
Calculator Module
------------------

This module provides basic arithmetic operations.

Functions:
1. add(x, y): Returns the sum of x and y.
2. subtract(x, y): Returns the difference between x and y.
3. multiply(x, y): Returns the product of x and y.
4. divide(x, y): Returns the division of x by y. Raises ValueError if y is zero.

Example Usage:
    from calc import add, subtract, multiply, divide
    print(add(10, 5))          # Output: 15
    print(divide(10, 0))       # Raises ValueError: "Can not divide by zero!"
"""

def add (x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function """
    return x - y

def multiply(x, y):
    """ Multiple Function """
    return x * y

def divide(x, y):
    """ Divide Function  """
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y

# print(add(10, 5))
# print(subtract(10, 5))
# print(multiply(10, 5))
# print(divide(10, 5))