#!/usr/bin/python3
''' return file  '''
import json


def from_json_string(my_str):
    ''' json string'''
    return json.load(my_str)
