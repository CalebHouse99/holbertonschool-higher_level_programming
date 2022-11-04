#!/usr/bin/python3
"""Second web scrape"""
if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
