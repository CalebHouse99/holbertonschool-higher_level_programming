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
        self.attrs = attrs
        at_list = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in self.__dict__:
                at_list[i] = self.__dict__[i]
        return at_list
