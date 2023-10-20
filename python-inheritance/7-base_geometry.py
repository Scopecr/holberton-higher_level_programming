#!/usr/bin/python3
"""
adding on to BaseGeometry
"""


class BaseGeometry:
    """
    Defines BaseGeometry
    """
    def area(self):
        """
        Raises:
            Exception: if area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates: if value is a integer and bigger than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be and integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
