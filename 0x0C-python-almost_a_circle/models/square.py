#!/usr/bin/python3
''' module Square '''

from .rectangle import Rectangle


class Square(Rectangle):
    ''' class square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' method built square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".
                format(__class__.__name__,
                       self.id, self.x, self.y, self.height))
