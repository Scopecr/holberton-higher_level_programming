#!/usr/bin/python3
"""
Attribute lookup object and methods
"""
def lookup(obj):
    """
    Function that returns the list of object
    """
    return [i for i in dir(obj)]
