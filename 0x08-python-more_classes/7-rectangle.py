#!/usr/bin/python3
'''Class rectangle'''


class Rectangle:
    '''Form'''
    print_symbol = '#   '
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Constructor'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Get the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''Get the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

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
        """string represention for information about
        """
        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        ''' repr '''
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        ''' method del and number of instances'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1


my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")
