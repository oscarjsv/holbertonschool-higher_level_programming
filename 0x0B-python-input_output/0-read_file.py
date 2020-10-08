#!/usr/bin/python3
''' module read '''


def read_file(filename=""):
    ''' read file '''
    with open('my_file_0.txt', encoding='utf-8') as reader:
        print(reader.read())
