#!/usr/bin/python3
"""Write to text file from object
"""
import json


def save_to_json_file(my_obj, filename):
    """Write to text file from object"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
