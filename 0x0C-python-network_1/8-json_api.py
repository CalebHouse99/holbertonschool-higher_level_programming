#!/usr/bin/python3
"""Json api, sends post request"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    req = requests.post(url, data={'q': q})
    try:
        dict = req.json()
        id = dist.get('id')
        name = dict.get('name')
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as e:
        print("Not a valid JSON")
