#!/usr/bin/python3

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

export_filename = "add_item.json"

try:
    buffer = load_from_json_file(export_filename)
except FileNotFoundError:
    buffer = []

for arg in sys.argv[1:]:
    buffer.append(arg)

save_to_json_file(buffer, export_filename)
