#!/usr/bin/python3
"""Student"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class to json"""
        if attrs is None:
            return (vars(self))
        attributes = {}
        for key, value in vars(self).items():
            if key in attrs:
                attributes[key] = value
        return (attributes)
