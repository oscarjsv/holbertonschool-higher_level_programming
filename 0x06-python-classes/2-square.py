#!/usr/bin/python3
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
