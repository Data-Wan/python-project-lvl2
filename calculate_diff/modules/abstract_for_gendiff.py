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


def gen_diff_dict(dict1, dict2):
    """Generate list with changes of 2 dictionaries.

    Args:
        dict1: dict
        dict2: dict

    Returns:
        list with changes: list
    """
    list_with_changes = []
    all_keys = union_keys(dict1, dict2)

    for key in all_keys:
        old_value = js_format_get(dict1, key)
        new_value = js_format_get(dict2, key)
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            list_with_changes.append({
                'name': key,
                'type': 'nested',
                'children': gen_diff_dict(old_value, new_value),
            })

        else:
            list_with_changes.append({
                'name': key,
                'type': 'value',
                'value': [old_value, new_value],
            })
    return list_with_changes
