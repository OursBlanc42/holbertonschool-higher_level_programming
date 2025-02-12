#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename=None):

    with open('data.csv', encoding='utf-8', newline='') as csvfile:

        csv_reader = csv.DictReader(csvfile)

        data = []
        for row in csv_reader:
            data.append(row)

    with open("data.json", "w", encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(data))
