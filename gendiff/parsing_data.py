# -*- coding:utf-8 -*-

"""
Parsing data from files.

Acceptable formats: .json, .yml
"""

import json

import yaml


def get_data(data_from_file, file_format):
    """Pars data from a file.

    Args:
        data_from_file: any file
        file_format: str

    Returns:
        dictionary with data: dict
    """
    if file_format == '.json':

        return json.load(data_from_file)
    elif file_format == '.yml':
        return yaml.load(data_from_file, Loader=yaml.SafeLoader)
    else:
        print('Oops!  That was no valid file format.  Try again...')  # noqa: WPS421, E501
