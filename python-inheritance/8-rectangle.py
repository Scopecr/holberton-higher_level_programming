#!/usr/bin/python3
"""
This script is for creating a Rectangle that inherits from circle
"""


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