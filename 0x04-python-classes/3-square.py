#!/usr/bin/python3
"""Class is defined as 'Square'"""


class Square:
    """This is the prototype"""
    def __init__(self, size=0):
        """ This is the initialization of self
        Args:
            size (int, optional): size of the square. Defaults to 0."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area"""
        return (self.__size ** 2)
