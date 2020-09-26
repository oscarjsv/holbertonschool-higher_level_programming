#!/usr/bin/python3
"""module say my name
    """


def say_my_name(first_name, last_name=""):
    """[summary]

    Args:
        first_name ([str]): [description]
        last_name (str, optional): [description]. Defaults to "".

    Raises:
        TypeError: [first_name must be a string]
        TypeError: [last_name must be a string]
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
