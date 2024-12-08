def mystery_3(a, b):
    """ This function compares two numbers and returns a value based on their relationship
    
    - if a is smaller than b it will return a
    - else if a greater than b it will return b
    - if a equals to b return the sum of the two values
    
    Parameters:
    - a int/float - first number
    - b int/float - second number

    Returns:
    int/float: returns the result based on the condition

    Examples:
    mystery_3(3, 5) -> 3
    mystery_3(7, 5) -> 5
    mystery_3(5, 5) -> 10

    """

    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
    

print(mystery_3(3, 5))