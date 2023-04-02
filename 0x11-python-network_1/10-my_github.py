#!/usr/bin/python3
"""
Python script that takes a Github creds (username and password) and uses the Github API to display user ID
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
