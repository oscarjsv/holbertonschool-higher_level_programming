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
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' class method save file '''

        filename = cls.__name__ + ".json"
        num = []
        if list_objs is not None:
            for obj in list_objs:
                num.append(cls.to_dictionary(obj))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(num))
    
    @staticmethod
    def from_json_string(json_string):
        ''' from json string '''
        json_list = []
        if not json_string:
            return json_list
        return  json.loads(json_string)