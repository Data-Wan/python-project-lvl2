# -*- coding:utf-8 -*-

"""Module with json formatter."""
import json


def jsonify(list_with_changes):  # noqa: WPS210
    """
    Turn dictionary into text with json format.

    Args:
        list_with_changes: dict

    Returns:
        str
    """
    return json.dumps(list_with_changes)
