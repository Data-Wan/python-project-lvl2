# -*- coding:utf-8 -*-

"""
Parsing data from files.

Acceptable formats: .json, .yml
"""

import json
import yaml


def parser(file_path):
    if file_path.endswith('json'):
        with open(file_path) as json_file:
            return json.load(json_file)
    elif file_path.endswith('yml'):
        with open(file_path) as yaml_file:
            return yaml.load(yaml_file, Loader=yaml.SafeLoader)
