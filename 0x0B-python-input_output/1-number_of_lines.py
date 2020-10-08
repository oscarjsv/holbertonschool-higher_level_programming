#!/usr/bin/python3
''' number of lines '''


def number_of_lines(filename=""):
    ''' number of lines '''
    with open(filename, 'r', encoding='utf-8') as read_l:
        return len(read_l.readlines())
