#!/usr/bin/python3
def inherits_from(obj, c_class):
    """Check if an object or class inherits from a given class."""
    return isinstance(obj, type) and issubclass(obj, c_class)

