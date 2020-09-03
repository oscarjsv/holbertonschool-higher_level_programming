#!/usr/bin/python3
import sys
from sys import argv

if __name__ == "__main__":
    count = 0
    for i in range(1, len(argv)):
        count += int(argv[i])
    print('{}'.format(count))
