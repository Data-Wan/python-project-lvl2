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
        for change in list_with_changes:
            name = '{0}{1}'.format(path, change.get('name'))
            if change.get('type') == 'value':
                [old_value, new_value] = change.get('value')
                if old_value != new_value:
                    output.append(create_row(name, old_value, new_value))
                continue
            children = change.get('children')
            output.append(walk(children, '{0}.'.format(name)))
        return '\n'.join(output)

    return walk(iterable)


def create_row(name, old_value, new_value):
    """Create a row for gendiff.

    Args:
        name: str
        old_value: any
        new_value: any

    Returns:
        formated string rows: str
    """
    old_value = turn_value_to_right_format(old_value)
    new_value = turn_value_to_right_format(new_value)
    template_added = (
        "Property '{0}' was added with value: {1}".format(name, new_value)
    )
    template_removed = (
        "Property '{0}' was removed".format(name)
    )
    template_updated = (
        "Property '{0}' was updated. From {1} to {2}".format(name, old_value, new_value)  # noqa: E501
    )

    if new_value is None:
        return template_removed  # current_indent, key, value
    elif old_value is None:
        return template_added  # current_indent, key, value
    elif old_value != new_value:
        return template_updated


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


def turn_value_to_right_format(elem):
    """Return value with js types check.

    Args:
        elem: any

    Returns:
        formated string rows: str
    """
    if is_nested(elem):
        return '[complex value]'
    elif is_str(elem):
        return "'{0}'".format(elem)
    return elem
