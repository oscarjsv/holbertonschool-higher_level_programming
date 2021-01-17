#!/usr/bin/python3
"""Error code #0"""

from urllib import request, parse, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as error:
        print("Error code:", error.code)
