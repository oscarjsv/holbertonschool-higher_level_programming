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
        ''' return representation of a student '''
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic