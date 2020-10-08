#!/usr/bin/python3
''' write the line '''


def write_file(filename="", text=""):
    ''' write file '''

    with open(filename, 'w', encoding='utf-8') as writer:
        return writer.write(text)
