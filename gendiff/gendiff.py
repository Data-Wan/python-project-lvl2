# -*- coding:utf-8 -*-

"""Module with main function."""

from pathlib import Path

from gendiff import formatters
from gendiff.abstract_for_gendiff import gen_diff_dict
from gendiff.formatters.parsing_data import get_data


def generate_diff(first_file, second_file, formatter='stylish'):  # noqa: WPS210
    """Determine the difference of 2 json files.

    Args:
        formatter: function
        first_file: dict
        second_file: dict

    Returns:
        string with difference: str
    """
    all_formatters = {
        'plain': formatters.plain,
        'stylish': formatters.stylish,
        'json': formatters.jsonify,
    }
    formatter = all_formatters.get(formatter)
    with open(first_file) as f1:
        dictionary1 = get_data(f1, Path(first_file).suffix)
    with open(second_file) as f2:
        dictionary2 = get_data(f2, Path(second_file).suffix)
    dict_with_changes = gen_diff_dict(dictionary1, dictionary2)
    return formatter(dict_with_changes)
