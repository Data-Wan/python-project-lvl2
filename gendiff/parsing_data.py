# -*- coding:utf-8 -*-

"""
Parsing data from files.

Acceptable formats: .json, .yml
"""

import json

import yaml


def get_data(data, file_format):  # noqa: WPS110
    """Pars data from a file.

    Args:
        data: any file
        file_format: str

    Returns:
        dictionary with data: dict
    """
    if file_format == '.json':
        return json.load(data)
    elif file_format == '.yml':
        return yaml.load(data, Loader=yaml.SafeLoader)
