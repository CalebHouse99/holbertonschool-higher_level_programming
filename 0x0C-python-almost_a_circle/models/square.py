#!/usr/bin/python3
""" Class of Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class of Square, inheriting Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the self"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding the str method"""
        a = "[Square] (" + str(self.id) + ") " + str(self.x) + "/"
        b = a + str(self.y) + " - " + str(self.width) + "/" + str(self.height)
        return b
