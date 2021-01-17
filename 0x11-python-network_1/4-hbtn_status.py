#!/usr/bin/python3
"""What's my status? #1"""

import requests

r = requests.get("https://intranet.hbtn.io/status")
print("Body response:\n\t- type: {}\n\t- content: {}"
      .format(type(r.text), r.text))
