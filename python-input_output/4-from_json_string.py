#!/usr/bin/python3
"""
Imports json file and returns an object from string
"""
import json


def from_json_string(my_str):
    """Convert a JSON string to an object."""
    return json.loads(my_str)
