#!/usr/bin/python3

import json
import sys
import os


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file

    Args:
        my_obj (obj): object we want to save
        filename (_type_): file name
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile, indent=4)


def load_from_json_file(filename):
    """
    load_from_json_file

    Args:
        filename (string): filename

    Returns:
        obj: python object load from a json file
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        python_object = json.load(myfile)
        return python_object


export_filename = "add_item.json"

# Check if the file exist
if os.path.isfile(export_filename) is True:
    buffer = load_from_json_file(export_filename)
else:
    buffer = []

for arg in sys.argv[1:]:
    buffer.append(arg)

save_to_json_file(buffer, export_filename)
