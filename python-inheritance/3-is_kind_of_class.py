#!/usr/bin/python3
"""
    Function that returns true if the object is an instance of
    or if object is a instance of a class that inherited from specified class
    otherwise false
    """


def is_kind_of_class(obj, a_class):
        if isinstance(obj) and issubclass(obj):
            return True
        else:
            return False
