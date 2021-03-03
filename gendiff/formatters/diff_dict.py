# -*- coding:utf-8 -*-

"""Module with generating diff_dict for gendiff."""


def gen_diff_dict(dict1, dict2):  # noqa: WPS210, WPS231
    """Generate list with changes of 2 dictionaries.

    Args:
        dict1: dict
        dict2: dict

    Returns:
        list with changes: list
    """
    difference = []
    all_keys = union_keys(dict1, dict2)
    no_value = object()
    for key in all_keys:
        old_value = dict1.get(key, no_value)
        new_value = dict2.get(key, no_value)
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            difference.append({
                'name': key,
                'type': 'NESTED',
                'children': gen_diff_dict(old_value, new_value),
            })

        elif old_value == no_value:
            difference.append({
                'name': key,
                'type': 'ADDED',
                'new_value': new_value,
            })
        elif new_value == no_value:
            difference.append({
                'name': key,
                'type': 'REMOVED',
                'old_value': old_value,
            })
        elif new_value == old_value:
            difference.append({
                'name': key,
                'type': 'UNCHANGED',
                'new_value': new_value,
            })
        else:
            difference.append({
                'name': key,
                'type': 'CHANGED',
                'new_value': new_value,
                'old_value': old_value,
            })
    return difference


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
