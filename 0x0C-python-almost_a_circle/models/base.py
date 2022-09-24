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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json string representation of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json string representation of an object to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns list from json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with atts set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                pumpkin = cls(2693877, 21736)
            else:
                pumpkin = cls(6)
            pumpkin.update(**dictionary)
            return pumpkin
