#!/usr/bin/python3
"""modulo 0 rectangle
    """


class Rectangle:
    """class rectangle
    """

    def __init__(self, width=0, height=0):
        """[constructor]

        Args:
            width (int, optional): [description]. Defaults to 0.
            height (int, optional): [description]. Defaults to 0.
        """
        self.width = width
        self.height = height

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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('heigth must be >= 0')
        
        self.__height = value
