# -*- coding:utf-8 -*-

"""Module with json formatter."""
import json


def jsonify(iterable):  # noqa: WPS210
    """Turn dictionary into text with json format.

    Args:
        iterable: dict

    Returns:
        str
    """

    def walk(list_with_changes):  # noqa: WPS430, WPS210
        output = {}
        for change in list_with_changes:
            key = '{0}'.format(change.get('name'))
            if change.get('type') == 'value':
                [old_value, new_value] = change.get('value')
                output.update(generate_key_val(key, old_value, new_value))
                continue
            children = change.get('children')
            output.update({'{0}'.format(key): walk(children)})
        return output

    return json.dumps(walk(iterable))


def generate_key_val(key, old_value, new_value):
    """Generate dict with changes of 1 key.

    Args:
        key: any
        old_value: any
        new_value: any

    Returns:
        dict
    """
    old_value = turn_value_to_right_format(old_value)
    new_value = turn_value_to_right_format(new_value)
    template_added = {'+ {0}'.format(key): new_value}
    template_removed = {'- {0}'.format(key): old_value}
    template_updated = (
        {'- {0}'.format(key): old_value, '+ {0}'.format(key): new_value}
    )
    if new_value is None:
        return template_removed  # current_indent, key, value
    elif old_value is None:
        return template_added  # current_indent, key, value
    elif old_value != new_value:
        return template_updated
    return {'{0}'.format(key): new_value}


def turn_value_to_right_format(elem):
    """Check if elem string without some special values.

    Args:
        elem: any

    Returns:
        any: right formatted value
    """
    if elem == 'null':
        return None
    elif elem == 'true':
        return True
    elif elem == 'false':
        return False
    return elem
