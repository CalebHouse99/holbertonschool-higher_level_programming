#!/usr/bin/python3
"""First web scrape"""
if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        response = response.read()
        print("    - type: {}".format(str(type(response))))
        print("    - content: {}".format(str(response)))
        print("    - utf8 content: {}".format(response.decode('utf-8')))
