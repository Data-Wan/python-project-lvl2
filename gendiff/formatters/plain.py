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
            new_value = to_str(node.get('new_value', object()))
            old_value = to_str(node.get('old_value', object()))
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


def to_str(elem):
    """Return value with js types check.

    Args:
        elem: any

    Returns:
        formatted string rows: str
    """
    special_value = {'True': 'true', 'False': 'false', 'None': 'null'}

    if isinstance(elem, (dict, list, tuple, set)):
        return '[complex value]'

    if str(elem) in special_value.keys():
        return special_value.get(str(elem))
    if isinstance(elem, str):
        return "'{0}'".format(elem)
    return elem
