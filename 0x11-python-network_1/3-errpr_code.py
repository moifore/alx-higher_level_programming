#!/usr/bin/python3
"""Displays the response body from a given URL
Usage: ./3-error_code.py <URL>
- Handles HTTP errors.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
