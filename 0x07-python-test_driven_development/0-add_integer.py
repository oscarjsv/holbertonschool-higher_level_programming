#!/usr/bin/python3
"""module number 0
    """


def add_integer(a, b=98):
    """[summary]

    Args:
        a (int) : [sum a int]
        b (int): [sum b int]. Defaults to 98.
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    if type(a) == float:
        type(a) == int
    if type(b) == float:
        type(b) == int

    return(a + b)
