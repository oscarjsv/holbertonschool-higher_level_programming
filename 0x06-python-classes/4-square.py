#!/usr/bin/python
""" this a comment in python"""


class Square:
    ''' class square '''

    def __init__(self, size=0):
        ''' init built '''
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter

        Args:
            value (value): [value of the square]

        Raises:
            TypeError: [size must be an integer]
            ValueError: [size must be >= 0]
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """area de size
        """
        return self.__size ** 2
