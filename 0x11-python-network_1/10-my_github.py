#!/usr/bin/python3
"""My Github!"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    r = requests.get(url, auth=auth)
    try:
        print(r.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
