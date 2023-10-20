#!/usr/bin/python3
""""""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
    """

    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
            width (int): method
            height (int): method
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height


    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """returns string with rectangle values"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
