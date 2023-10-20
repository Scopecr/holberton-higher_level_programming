#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Check if an object or class inherits from a given class."""
    return (type(obj)) is not a_class and issubclass(type(obj), a_class)

