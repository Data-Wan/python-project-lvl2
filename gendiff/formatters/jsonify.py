# -*- coding:utf-8 -*-

"""Module with json formatter."""
import json


def jsonify(iterable):  # noqa: WPS210
    """
    Turn dictionary into text with json format.

    Args:
        iterable: dict

    Returns:
        str
    """

    def walk(list_with_changes):  # noqa: WPS430, WPS210
        output = {}
        for node in list_with_changes:
            old_value = node.get('old_value')
            new_value = node.get('new_value')
            name = node.get('name')
            type_of_node = node.get('type')
            if type_of_node == 'NESTED':
                nested_lines = walk(node.get('children'))
                output.update(
                    {name: nested_lines},
                )
            else:
                output.update(create_dict_with_change(name, old_value, new_value, type_of_node))  # noqa: E501

        return output

    return json.dumps(walk(iterable))


def create_dict_with_change(name, old_value, new_value, type_of_node):
    """Create a dict with changes - python format.

    Args:
        name: str
        old_value: any
        new_value: any
        type_of_node: str

    Returns:
        dict to string: str
    """
    if type_of_node == 'REMOVED':
        return {'- {0}'.format(name): old_value}

    elif type_of_node == 'ADDED':
        return {'+ {0}'.format(name): new_value}

    elif type_of_node == 'CHANGED':
        return {
            '- {0}'.format(name): old_value,
            '+ {0}'.format(name): new_value,
        }

    return {name: new_value}
