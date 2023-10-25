#!/usr/bin/python3
"""
Rectangle class that inherits from Base
"""
from.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init Class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Width Getter
        """
        return self._width

    @property
    def height(self):
        """
        Height Getter
        """
        return self.__height

    @property
    def x(self):
        """
        x Getter
        """
        return self.__x

    @property
    def y(self):
        """
        y Getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Width Setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value myst be > 0
        """
        if type (value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be greater than zero")
        self._width = value

    @height.setter
    def height(self, value):
        """
        height setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: is not integer
            ValueError: must be > 0
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        x Setter
        Attributes:
            value(int): value assign
        Raises:
            TypeError: is not integer
            ValueError: must be > 0
        """
        if type(value) is not int:
            raise TypeError("X coordinate must be an integer")
        if value <= 0:
            raise ValueError("X coordinate must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Y Setter
        Attributes:
            Value(int):value assigned
        Raises:
            TypeError: if not integer
            ValueError: must be > 0
        """
        if type(value) is not int:
            raise TypeError("Y coordinate must be an integer")
        if value <= 0:
            raise ValueError("Y is must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculation of area of rectangle
        """
        self.__width * self.__height

    def display(self):
        """display the Rectangle using '#' """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        String Informal of the Rectangle
        """
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        if args:
            self.id, self.width, self.height, self.x, self.y = args
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary
        representation of a rectangle
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
