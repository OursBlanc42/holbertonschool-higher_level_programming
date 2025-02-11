#!/usr/bin/python3

import xml.etree.ElementTree as ET
import json


def serialize_to_xml(dictionary, filename):
    """
    serialize_to_xml write XML in specify file

    Args:
        dictionary (dict): data
        filename (string): filename
    """
    root_element = "<data>"


def deserialize_from_xml(filename):

    # create a tree from xmml
    tree = ET.parse(filename)

    # catch the root
    root = tree.getroot()

    my_dict = {}

    for child in root:
        my_dict[child.tag] = child.text
