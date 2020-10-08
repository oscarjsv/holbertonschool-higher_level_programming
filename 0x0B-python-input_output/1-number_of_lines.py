#!/usr/bin/python3
''' number of lines '''


def number_of_lines(filename=""):
    ''' number of lines '''
    with open('my_file_0.txt', 'r', encoding='utf-8') as read_l:
        return len(read_l.readlines())
