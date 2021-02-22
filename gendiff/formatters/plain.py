# -*- coding:utf-8 -*-

"""Module with plain formatter."""


def plain(iterable):  # noqa: WPS210
    """Turn dictionary into strings with plain format.

    Args:
        iterable: dict

    Returns:
        str
    """

    def walk(list_with_changes, path=''):  # noqa: WPS430, WPS210
        output = []
        for node in list_with_changes:
            name = path + node['name']
            new_value = to_str(get_convert_js(node, 'new_value'))
            old_value = to_str(get_convert_js(node, 'old_value'))
            templates = {
                'REMOVED': "Property '{0}' was removed".format(name),
                'ADDED': "Property '{0}' was added with value: {2}",
                'CHANGED': "Property '{0}' was updated. From {1} to {2}",
            }
            type_of_node = node['type']
            if type_of_node == 'NESTED':
                nested_lines = walk(node['children'], '{0}.'.format(name))
                output.append(nested_lines)
            elif type_of_node != 'UNCHANGED':
                output.append(templates.get(type_of_node).format(name, old_value, new_value))  # noqa: E501

        return '\n'.join(output)

    return walk(iterable)


def is_nested(elem):
    """Check if elem nested or not.

    Args:
        elem: any

    Returns:
        bool: true == nested, false == not
    """
    return isinstance(elem, (dict, list, tuple, set))


def is_str(elem):
    """Check if elem string without some special values.

    Args:
        elem: any

    Returns:
        bool
    """
    not_special_value = elem not in {'null', 'true', 'false'}
    return not_special_value and isinstance(elem, str)


def to_str(elem):
    """Return value with js types check.

    Args:
        elem: any

    Returns:
        formatted string rows: str
    """
    if is_nested(elem):
        return '[complex value]'
    elif is_str(elem):
        return "'{0}'".format(elem)
    return elem


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
