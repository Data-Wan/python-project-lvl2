# -*- coding:utf-8 -*-

"""Module with formatters."""


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
        output = ['{', '{0}{1}'.format(replacer * depth, '}')]
        depth += 1
        for change in list_with_changes:
            name = change.get('name')
            if change.get('type') == 'value':
                [old_value, new_value] = change.get('value')
                output.insert(
                    -1, create_row(replacer, depth, name, old_value, new_value),
                )
                continue
            children = change.get('children')
            output.insert(
                -1, '{0}  {1}: {2}'.format(
                    replacer * depth,
                    name,
                    walk(children, depth + 1),
                ))
        return '\n'.join(output)

    return walk(iterable, 0)


def create_row(replacer, depth, key, old_value, new_value):
    """Create a row for gendiff.

    Args:
        replacer: str
        depth: int
        key: any
        old_value: any
        new_value: any

    Returns:
        formated string rows: str
    """
    template_nothing = (
        '{0}  {1}: {2}'.format(replacer * depth, key, stringify_dict(
            old_value, depth + 1, replacer,
        ))
    )
    template_deleted = (
        '{0}- {1}: {2}'.format(replacer * depth, key, stringify_dict(
            old_value, depth + 1, replacer,
        ))
    )
    template_added = (
        '{0}+ {1}: {2}'.format(replacer * depth, key, stringify_dict(
            new_value, depth + 1, replacer,
        ))
    )
    if new_value is None:
        return template_deleted  # current_indent, key, value
    elif old_value is None:
        return template_added  # current_indent, key, value
    elif old_value != new_value:
        return '{0}\n{1}'.format(template_deleted, template_added)
    return template_nothing  # current_indent, key, value


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
