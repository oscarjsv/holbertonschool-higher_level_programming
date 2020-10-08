#!/usr/bin/python3
''' save to json '''

import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Args:
        my_obj (dict ):
        filename (file empty)
    """
    with open(filename, 'w', encoding='utf') as writer:
        return json.dump(my_obj, writer)
