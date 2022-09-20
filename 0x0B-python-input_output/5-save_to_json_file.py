#!/usr/bin/python3
"""Write to text file from object
"""
import json


def save_to_json_file(my_obj, filename):
    """Write to text file from object"""
    jason_string = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(jason_string)
        file.close
