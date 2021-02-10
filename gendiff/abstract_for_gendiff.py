# -*- coding:utf-8 -*-

"""Module with abstract functions for generate_diff."""


def js_format_get(dictionary, key):
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
