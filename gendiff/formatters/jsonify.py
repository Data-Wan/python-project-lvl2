# -*- coding:utf-8 -*-

"""Module with json formatter."""
import json


def jsonify(difference):  # noqa: WPS210
    """
    Turn dictionary into text with json format.

    Args:
        difference: dict

    Returns:
        str
    """
    return json.dumps(difference)
