# -*- coding:utf-8 -*-

"""Module with stylish formatter."""
from gendiff.formatters.plain import get_convert_js


def stylish(iterable, replacer='  '):  # noqa: WPS210
    """
    Turn dictionary into strings with json.stringify.

    Args:
        iterable: dict
        replacer: str

    Returns:
        str
    """

    def walk(list_with_changes, depth=0):  # noqa: WPS430, WPS210
        output = ['{']
        depth += 1
        current_indent = replacer * depth

        for node in list_with_changes:
            type_of_node = node.get('type')
            old_value = get_convert_js(node, 'old_value')
            new_value = get_convert_js(node, 'new_value')
            old_value = stringify_dict(old_value, depth + 1, replacer)
            new_value = stringify_dict(new_value, depth + 1, replacer)
            name = node.get('name')
            templates = {
                'REMOVED': '{0}- {1}: {2}',
                'ADDED': '{0}+ {1}: {3}',
                'UNCHANGED': '{0}  {1}: {3}',
                'CHANGED': '{0}- {1}: {2}\n{0}+ {1}: {3}',
            }
            if node['type'] == 'NESTED':
                nested_lines = walk(node['children'], depth + 1)
                output.append(
                    '{0}  {1}: {2}'.format(current_indent, name, nested_lines),
                )
            else:
                output.append(
                    templates.get(type_of_node).format(current_indent, name, old_value, new_value),  # noqa: E501
                )
        output.append('{0}{1}'.format(replacer * (depth - 1), '}'))
        return '\n'.join(output)

    return walk(iterable, 0)


def stringify_dict(collection, depth, replacer):  # noqa: WPS210
    """Turn dictionary into strings with json.stringify.

    Args:
        collection: dict
        replacer: str
        depth: int

    Returns:
        dict to string: str
    """
    if not isinstance(collection, dict):
        return str(collection)
    output = ['{', '{0}{1}'.format(replacer * depth, '}')]
    depth += 1
    for key, value in collection.items():  # noqa: WPS110
        row = '{0}  {1}: {2}'.format(replacer * depth, key, stringify_dict(
            value, depth + 1, replacer,
        ))
        output.insert(-1, row)
    return '\n'.join(output)
