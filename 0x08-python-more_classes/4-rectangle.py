#!/usr/bin/python3
"""modulo 0 rectangle
    """


class Rectangle:
    """class rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """[constructor]

        Args:
            width (int, optional): [description]. Defaults to 0.
            height (int, optional): [description]. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width property

        Returns:
            [__width]: [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        ''' widht '''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        ''' heigth'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        ''' return the area  '''
        return self.__width * self.__height

    def perimeter(self):
        ''' perimeter '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        ''' str metodo '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        ''' repr '''
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
