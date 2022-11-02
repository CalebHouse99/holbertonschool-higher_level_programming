#!/usr/bin/python3
"""Get post request"""
if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse
    import urllib

    values = {}
    print('open is assigned to %r' % open)
    with request.Request(argv[1], method="POST") as req:
        r = request.urlencode(values)
        req = urllib.request.Request(argv[1], values)
        print(req)
