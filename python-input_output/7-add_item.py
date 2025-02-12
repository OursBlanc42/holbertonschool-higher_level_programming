#!/usr/bin/python3
"""
    adds all arguments to a Python list, and then save them to a file:
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

export_filename = "add_item.json"

if os.path.isfile(export_filename) is True:
    buffer = load_from_json_file(export_filename)
else:
    buffer = []

for arg in sys.argv[1:]:
    buffer.append(arg)

save_to_json_file(buffer, export_filename)
