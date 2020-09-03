#!/usr/bin/python3
import sys

from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print('{} arguments. '.format(len(sys.argv)-1))
    elif len(argv) == 2:
        print('{} argument: '.format(len(sys.argv)-1))
    else:
        print('{} arguments: '.format(len(sys.argv)-1))
    for i in range(1, len(argv)):
        print('{}: {}'.format(i, argv[i]))
