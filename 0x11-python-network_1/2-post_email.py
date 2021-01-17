#!/usr/bin/python3
"""POST an email #0"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], data)
    with request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
