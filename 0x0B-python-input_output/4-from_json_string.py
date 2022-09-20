#!/usr/bin/python3
"""Return object
"""
import json


def from_json_string(my_str):
    """Return object"""
    object = json.loads(my_str)
    return object
