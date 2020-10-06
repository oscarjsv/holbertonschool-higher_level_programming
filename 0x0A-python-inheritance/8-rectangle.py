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
    """ Rectangles

    Args:
        BaseGeometry (subclass): [description]
    """

    def __init__(self, width, height):
        ''' method init '''
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
