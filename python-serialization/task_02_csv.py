#!/usr/bin/python3

"""
    reading data from one format (CSV) and converting it into
    another format (JSON) using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(filename=None):
    """
    convert_csv_to_json

    Args:
        filename (_type_, optional): _description_. Defaults to None.
    """

    with open(filename, encoding='utf-8', newline='') as csvfile:

        csv_reader = csv.DictReader(csvfile)

        data = []
        for row in csv_reader:
            data.append(row)

    with open("data.json", "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4)
