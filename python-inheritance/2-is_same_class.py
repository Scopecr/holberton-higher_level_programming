#!/usr/bin/python3
"""
Define a function that returns True if the object is exactly an instance
of the specified class; otherwise False
"""
def is_same_class(obj, a_class):
    """
    Return True if is instance return else return false_
    """
    return type(obj) is a_class
