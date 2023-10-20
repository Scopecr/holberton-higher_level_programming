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
        if type(value) is not int:
            TypeError("{} must be and integer".format(name))
        if value <= 0:
            ValueError("{} must be greater than 0".format(name))
