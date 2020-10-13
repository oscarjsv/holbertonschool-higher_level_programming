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
        s = '\n' * self.__y + \
            (' ' * self.__x + '#' * self.__width + '\n') * self.__height
        print(s, end='')

    def __str__(self):
        ''' method str '''
        return '[{}] ({}) {}/{} - {}/{}' .format(__class__.__name__,
                                                 self.id, self.__x, self.__y,
                                                 self.__width, self.__height)

    def update(self, *args, **kwargs):
        ''' method update '''
        if len(args):
            for idx, valor in enumerate(args):
                if idx == 0:
                    self.id = valor
                elif idx == 1:
                    self.__width = valor
                elif idx == 2:
                    self.__height = valor
                elif idx == 3:
                    self.__x = valor
                elif idx == 4:
                    self.__y = valor
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'widht':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y == value
