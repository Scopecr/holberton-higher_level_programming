#!/usr/bin/python3
"""Function that returns the JSON representation o an object"""
import json

def to_json_string(my_obj):
    """Returns a string with the json representation of my_obj."""
    return json.dumps(my_obj)
