#!/usr/bin/python3
"""Get variable in header"""
if __name__ == "__main__":
    from sys import argv
    from urllib import request
    from urllib.parse import urlparse, parse_qs
    
    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
