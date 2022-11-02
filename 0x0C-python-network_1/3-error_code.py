try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)