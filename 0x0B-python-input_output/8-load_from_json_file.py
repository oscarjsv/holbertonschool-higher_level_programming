#!/usr/bin/python3
''' loaf from json file '''

import json


def load_from_json_file(filename):
    """lod from json file

    Args:
        filename (file): [file saved the information]
    """

    with open(filename, 'r', encoding='utf-8') as reader:
        return json.load(reader)
