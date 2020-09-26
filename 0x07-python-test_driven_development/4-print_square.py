#!/usr/bin/python3
""" module 4
    """


def print_square(size):
    """[summary]

    Args:
        size ([type]): [description]

    Raises:
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
        TypeError: [size must be an integer]
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    size = int(size)
    for _ in range(size):
        print(size * '#')
