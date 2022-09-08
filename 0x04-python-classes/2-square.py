#!/usr/bin/python3
"""Class is defined as 'Square'"""


class Square:
    """This is the prototype"""
    def __init__(self, size=0):
        """ This is the initialization of self

        Args:
            size (int, optional): size of the square. Defaults to 0.
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
    """Return the area"""
    def area(self):
        a = self.__size * self.__size
        self.area = a
        return a
