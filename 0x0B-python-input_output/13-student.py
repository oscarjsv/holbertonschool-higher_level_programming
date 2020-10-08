#!/usr/bin/python3
''' 11 student '''


class Student:
    ''' class estudent '''

    def __init__(self, first_name, last_name, age):
        ''' method  built-in '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        class object type
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in self.__dict__:
                if i in attrs:
                    new_dict[i] = self.__dict__[i]
            return new_dict
    
    def reload_from_json(self, json):
            for k, v in json.items():
                if hasattr(self, k):
                    setattr(self, k, v)