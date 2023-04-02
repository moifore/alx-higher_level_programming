#!/usr/bin/python3
"""Scrpt that handles HTTP errors.

Usage: ./7-error_code.py <URL>
    - Handles HTTP erros.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    status = req.status_code
    print(req.text)
    
    if status >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
