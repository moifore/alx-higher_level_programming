#!/usr/bin/python3
"""Script takes in a <URL> and <email_address> and sends a POST request to the <URL> with the <email_address> as parameter.

Usage: ./6-post_email.py <URL> <email_address>
"""

import requests
from sys import argv

if __name__ == "__main__":
    email_address = {"Email": argv[2]}

    req = requests.post(argv[1], data=email_address)
    print(req.text)

