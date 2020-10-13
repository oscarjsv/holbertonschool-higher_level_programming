#!/usr/bin/python3
''' module rectangle '''

from .base import Base


class Rectangle(Base):
    ''' Class Rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' method built init'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' property widht '''
        return self.__width

    @property
    def height(self):
        ''' property height '''
        return self.__height

    @property
    def x(self):
        ''' property x '''
        return self.__x

    @property
    def y(self):
        ''' property y '''
        return self.__y

    @width.setter
    def width(self, width):
        ''' method setter width '''
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @height.setter
    def height(self, height):
        ''' method setter height '''
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        ''' method setter x '''
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        ''' method setter y '''
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        ''' method publir return area '''
        return self.__width * self.__height

    def display(self):
        ''' method display the stdout # '''
        print((('#' * self.__width + "\n") *
                self.__height)[:-1])
