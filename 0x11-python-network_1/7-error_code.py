#!/usr/bin/python3
"""Scrpt that handles HTTP errors.

Usage: ./7-error_code.py <URL>
    - Handles HTTP erros.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    status = r.status_code
    print(r.text)
    
    if status >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
