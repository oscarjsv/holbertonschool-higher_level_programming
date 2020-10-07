#!/usr/bin/python3
''' base geometry 8'''


class BaseGeometry:
    ''' base geometry '''

    def area(self):
        ''' method area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' integer validator '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    Arguments:
        BaseGeometry {class} -- super class
    """
    def __init__(self, width, height):
        """Rectangle with private height and width
        Arguments:
            width {int} -- Width of  the rectangle
            height {int} -- Height of  the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height