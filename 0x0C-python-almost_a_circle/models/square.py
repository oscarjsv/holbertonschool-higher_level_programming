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
        return self.width

    @size.setter
    def size(self, value):
        '''setter size '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' method update '''
        if len(args):
            for idx, valor in enumerate(args):
                if idx == 0:
                    self.id = valor
                if idx == 1:
                    self.size = valor
                if idx == 3:
                    self.__x = valor
                if idx == 4:
                    self.__y = valor
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
