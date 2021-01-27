# -*- coding:utf-8 -*-

"""Module with functions for gendiff.py."""

from calculate_diff.modules.parsing_data import parser


def generate_value_diff(dict1, dict2, key):
    """Generate list with difference of 2 dict with 1 key.

    Args:
        dict1: dict
        dict2: dict
        key: any

    Returns:
        list with difference: list
    """
    output = []
    if dict1.get(key, object) == object:
        output.append('  + {0}: {1}'.format(key, dict2.get(key)))
    elif dict2.get(key, object) == object:
        output.append('  - {0}: {1}'.format(key, dict1.get(key)))
    elif dict1.get(key) == dict2.get(key):
        output.append('    {0}: {1}'.format(key, dict1.get(key)))
    else:
        output.append('  - {0}: {1}'.format(key, dict1.get(key)))
        output.append('  + {0}: {1}'.format(key, dict2.get(key)))
    return output


def union_keys(dictionary1, dictionary2):
    """Generate list with union of 2 dictionaries`s keys.

    Args:
        dictionary1: dict
        dictionary2: dict

    Returns:
        list with keys: list

    """
    all_keys = set(dictionary1.keys()).union(set(dictionary2.keys()))
    return sorted(all_keys)


def generate_diff(first_file, second_file):  # noqa: WPS210
    """Determine the difference of 2 json files.

    Args:
        first_file: dict
        second_file: dict

    Returns:
        string with difference: str
    """
    dictionary1 = parser(first_file)
    dictionary2 = parser(second_file)
    all_keys = union_keys(dictionary1, dictionary2)

    output = ['{']
    for key in all_keys:
        output.extend(generate_value_diff(dictionary1, dictionary2, key))
    output.append('}')

    return '\n'.join(output)
