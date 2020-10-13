#!/usr/bin/python3
''' module Square '''

from .rectangle import Rectangle


class Square(Rectangle):
    ''' class square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' method built square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' '''
        return ("[{}] ({}) {}/{} - {}".
                format(__class__.__name__,
                       self.id, self.x, self.y, self.height))

    @property
    def size(self):
        ''' size'''
        return self.height

    @size.setter
    def size(self, value):
        '''setter size '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
            """Update the square with keyword-argument"""
            attributes = ['id', 'size', 'x', 'y']

            for idx, x in enumerate(args):
                if idx >= len(attributes):
                    return

                self.__setattr__(attributes[idx], x)

            if args:
                return

            for k, v in kwargs.items():
                self.__setattr__(k, v)