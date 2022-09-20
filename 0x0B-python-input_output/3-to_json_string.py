#!/usr/bin/python3
"""Return JSON representation
"""
import json


def to_json_string(my_obj):
    """Return JSON representation"""
    jason_string = json.dumps(my_obj)
    return jason_string
