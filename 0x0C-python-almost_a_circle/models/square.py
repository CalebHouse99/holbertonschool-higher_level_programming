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
        b = a + str(self.y) + " - " + str(self.height)
        return b

    @property
    def size(self):
        """Returning the size attribute"""
        return self.height

    @size.setter
    def size(self, value):
        """Setter of the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.size = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
