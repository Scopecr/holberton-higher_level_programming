#!/usr/bin/python3
"""Module that writes obj to a text"""
import json


def save_to_json_file(my_obj, filename):
    """Save an object into a JSON file."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
