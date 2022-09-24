#!/usr/bin/python3
""" Class of Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the self"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @property
    def x(self):
        """X of rectangle"""
        return self.__x

    @property
    def y(self):
        """y of rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter of the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter of the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area"""
        return self.height * self.width

    def display(self):
        """Prints out the rectangle"""
        for z in range(self.y):
            print("")
        for i in range(self.height):
            brick = ""
            for a in range(self.x):
                brick = brick + " "
            for j in range(self.width):
                brick = brick + "#"
            print(brick, end="\n")

    def __str__(self):
        """Overriding the str method"""
        a = "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/"
        b = a + str(self.y) + " - " + str(self.width) + "/" + str(self.height)
        return b

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        "Dictionary representation of Rectangle"
        rec_dictionary = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return rec_dictionary
