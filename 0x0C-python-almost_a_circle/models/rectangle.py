#!/usr/bin/python3
""" Class of Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the self"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the width"""
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of the height"""
        self.__height = value

    @property
    def x(self):
        """X of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of the x"""
        self.__x = value

    @property
    def y(self):
        """y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the y"""
        self.__y = value
