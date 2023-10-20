#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Importing from Rectangle"""
    def __init__(self, size):
        """_summary_

        Args:
            size (int): size must be positive
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """

        Returns:
            size: description of the area of square
        """
        return self.__size * self.__size
