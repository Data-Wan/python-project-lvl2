# -*- coding:utf-8 -*-

"""Module with abstract functions for generate_diff."""


def get_convert_js(dictionary, key):
    """Return value in js format.

    Args:
        dictionary: dict
        key: any

    Returns:
        value: any
    """
    if dictionary.get(key) is True:
        return 'true'
    elif dictionary.get(key) is False:
        return 'false'
    elif dictionary.get(key, object()) is None:
        return 'null'
    return dictionary.get(key)


def union_keys(dictionary1, dictionary2):
    """Generate list with union of 2 dictionaries`s keys.

    Args:
        dictionary1: dict
        dictionary2: dict

    Returns:
        list with sorted keys: list

    """
    all_keys = set(dictionary1.keys()).union(set(dictionary2.keys()))
    return sorted(all_keys)
