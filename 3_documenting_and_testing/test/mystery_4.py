def mystery_4(a):
    """
    Generates a list of integers starting from 0 up to (but not including) `a`.

    Parameters:
    - a (int): The length of the list to generate. Must be a non-negative integer.

    Returns:
    - list: A list containing integers from 0 to `a - 1`.

    Example:
    >>> mystery_4(5)
    [0, 1, 2, 3, 4]

    Function Details:
    - Initializes an empty list `b`.
    - Uses a variable `c` (initialized to 0) to track the next number to append.
    - keeps appending `c` to `b` and increments `c` by 1 until the length of `b` equals `a`.
    """

    
    if not isinstance(a, int):
        raise TypeError("Only integers are accepted")
    elif a < 0:
     raise ValueError("Negative numbers are not accepted")
    

    b = []

    c = 0

    while len(b) < a:
        b.append(c)
        c = c + 1

    return b

# print(mystery_4("a"))