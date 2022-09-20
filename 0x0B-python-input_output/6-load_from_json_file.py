#!/usr/bin/python3
"""Create object from JSON
"""
import json


def load_from_json_file(filename):
    """Create object from JSON"""
    with open(filename, 'r') as file:
        return json.load(file)
