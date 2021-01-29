# -*- coding:utf-8 -*-

"""Module with functions for gendiff.py."""

from calculate_diff.modules.abstract_for_gendiff import gen_diff_dict
from calculate_diff.modules.parsing_data import parser


def generate_diff(first_file, second_file, formatter):  # noqa: WPS210
    """Determine the difference of 2 json files.

    Args:
        formatter: function
        first_file: dict
        second_file: dict

    Returns:
        string with difference: str
    """
    dictionary1 = parser(first_file)
    dictionary2 = parser(second_file)
    dict_with_changes = gen_diff_dict(dictionary1, dictionary2)
    return formatter(dict_with_changes)
