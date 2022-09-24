#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Almost a Circle"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the self"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Json string representation of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string
