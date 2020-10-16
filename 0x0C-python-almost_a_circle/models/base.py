#!/usr/bin/python3
''' module base '''

import json
import os


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
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' method create '''
        if cls.__name__ == 'Rectangle':
            dummy = (cls(2, 2))
        if cls  .__name__ == 'Square':
            dummy = (cls(2))

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        new_instance = []
        filename = cls.__name__ + ".json"

        if not os.path.isfile(filename):
            return new_instance

        with open(filename, mode="r", encoding="utf-8") as newfile:
            new_instance = cls.from_json_string(newfile.read())
        return [cls.create(**dic) for dic in new_instance]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' class method save file '''

        filename = cls.__name__ + ".csv"
        num = []
        if list_objs is not None:
            for obj in list_objs:
                num.append(cls.to_dictionary(obj))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(num))
    
    @classmethod
    def load_from_file_csv(cls):
        """ returns a list of instances """
        new_instance = []
        filename = cls.__name__ + ".csv"

        if not os.path.isfile(filename):
            return new_instance

        with open(filename, mode="r", encoding="utf-8") as newfile:
            new_instance = cls.from_json_string(newfile.read())
        return [cls.create(**dic) for dic in new_instance]