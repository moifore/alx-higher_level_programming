#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as resp:
        body = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8)))
