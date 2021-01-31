# -*- coding:utf-8 -*-

"""Module with plain formatter."""


def plain(iterable):
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
    old_value = turn_value_to_right_format(old_value)
    new_value = turn_value_to_right_format(new_value)
    template_added = "Property '{0}' was added with value: {1}".format(name, new_value)
    template_removed = "Property '{0}' was removed".format(name)
    template_updated = (
        "Property '{0}' was updated. From {1} to {2}".format(name, old_value, new_value)
    )

    if new_value is None:
        return template_removed  # current_indent, key, value
    elif old_value is None:
        return template_added  # current_indent, key, value
    elif old_value != new_value:
        return template_updated


def is_nested(value):
    return (isinstance(value, dict)
            or isinstance(value, list)
            or isinstance(value, tuple)
            or isinstance(value, set))


def is_str(value):
    return (value != 'null'
            and value != 'true'
            and value != 'false'
            and isinstance(value, str))


def turn_value_to_right_format(value):
    if is_nested(value):
        return '[complex value]'
    elif is_str(value):
        return "'{0}'".format(value)
    return value
