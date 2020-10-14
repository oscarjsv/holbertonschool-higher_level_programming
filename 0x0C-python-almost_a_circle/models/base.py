#!/usr/bin/python3
''' module base '''

import json


class Base:
    """base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        ''' init built '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' json string '''
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)
