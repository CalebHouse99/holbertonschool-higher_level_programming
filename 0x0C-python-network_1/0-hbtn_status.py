#!/usr/bin/python3
"""First web scrape"""
if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        response = response.read()
        print("\t- type: {}".format(str(type(response))))
        print("\t- content: {}".format(str(response)))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
