
"""
Write a function that creates an Object from a “JSON file”:

Prototype: def load_from_json_file(filename):
You must use the with statement
You don’t need to manage exceptions if the JSON string doesn’t represent an object.
You don’t need to manage file permissions / exceptions.

"""

import json


def load_from_json_file(filename):
    """ my function """
    with open(filename) as file:
        return json.load(file)