#!/usr/bin/python3
""" Rectangle
"""


class Rectangle:
    """ Class of Rctangle """

    def __init__(self, width=0, height=0):
        """ Initialize Rectangle """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the Width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the Height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns Area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Returns Perimteter """
        if (self.__height * self.__width) == 0:
            return 0
        return (self.__height + self.__width) * 2
