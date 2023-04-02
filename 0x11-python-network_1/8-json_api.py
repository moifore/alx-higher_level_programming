#!/usr/bin/python3
"""
Script takes in a letter and submit a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter

Usage: ./8-json_api.py <letter>
"""

import requests
import sys

if __name__ == "__main__":
    q = argv[1] 
    if len(argv) == 2:
        print("'q': q")

    else:
        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, data={'q': q})
    
    try:
        r_dict = r.json()
        id, name = r_dict.get('id'), r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except:
        print("Not a valid JSON")
