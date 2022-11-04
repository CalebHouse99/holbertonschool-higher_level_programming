#!/usr/bin/python3
"""Get post request"""
if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse

    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
