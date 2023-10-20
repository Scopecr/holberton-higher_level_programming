#!/usr/bin/python3
"""
adding on to BaseGeometry
"""


class BaseGeometry:
    """
    Defines BaseGeometry
    """
    def area(self):
        """_summary_

        Raises:
            Exception: _description_
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            TypeError("{name} must be and integer")
        elif type(value) <= 0:
            ValueError("{name} must be greater than 0")
