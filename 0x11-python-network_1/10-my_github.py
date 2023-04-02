#!/usr/bin/python3
"""
Python script that takes a Github creds (username and password) and uses the Github API to display user ID
"""

import requests
from requests.auth import HTTPBasicAuth
from sys

if __name__ == "__main__":
    url = "https://api.github.comusers/{}".format(argv[1])
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get("id"))
