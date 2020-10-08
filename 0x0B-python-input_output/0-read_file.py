#!/usr/bin/python3
''' module read '''


def read_file(filename=""):
    ''' read file '''
    with open(filename, encoding='utf-8') as reader:
        for line in reader:
            print(line, end="")
