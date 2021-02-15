# -*- coding:utf-8 -*-

"""Module with main function."""

from pathlib import Path

from gendiff import formatters
from gendiff.parsing_data import get_data
from gendiff.tools_for_gendiff import union_keys


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


def gen_diff_dict(dict1, dict2):  # noqa: WPS210, WPS231
    """Generate list with changes of 2 dictionaries.

    Args:
        dict1: dict
        dict2: dict

    Returns:
        list with changes: list
    """
    list_with_changes = []
    all_keys = union_keys(dict1, dict2)
    no_value = object()
    for key in all_keys:
        old_value = dict1.get(key, no_value)
        new_value = dict2.get(key, no_value)
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            list_with_changes.append({
                'name': key,
                'type': 'NESTED',
                'children': gen_diff_dict(old_value, new_value),
            })

        elif old_value == no_value:
            list_with_changes.append({
                'name': key,
                'type': 'ADDED',
                'new_value': new_value,
            })
        elif new_value == no_value:
            list_with_changes.append({
                'name': key,
                'type': 'REMOVED',
                'old_value': old_value,
            })
        elif new_value == old_value:
            list_with_changes.append({
                'name': key,
                'type': 'UNCHANGED',
                'new_value': new_value,
            })
        else:
            list_with_changes.append({
                'name': key,
                'type': 'CHANGED',
                'new_value': new_value,
                'old_value': old_value,
            })
    return list_with_changes
