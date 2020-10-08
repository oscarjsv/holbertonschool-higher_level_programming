#!/usr/bin/python3
''' append line to the file '''


def append_write(filename="", text=""):
    ''' append write '''
    with open(filename, 'a') as append:
        return append.write(text)
