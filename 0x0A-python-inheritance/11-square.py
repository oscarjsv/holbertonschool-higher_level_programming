#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from rectangle
    Arguments:
        Rectangle {class} -- Class rectangle
    """
    def __init__(self, size):
        """ Square class that inherits from rectangle
        Arguments:
            size {int} -- size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        ''' method str'''
        return "[{}] {:d}/{:d}".format(__class__.__name__,
                                       self.__size, self.__size)