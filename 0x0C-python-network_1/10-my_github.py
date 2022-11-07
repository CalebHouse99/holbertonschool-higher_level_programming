#!/usr/bin/python3
"""Github credentials and API"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    url = ""
    username = argv[1]
    token = argv[2]
    req = requests.get(url, auth=HTTPBasicAuth(username, token)).json()
    print(req.get('id'))
