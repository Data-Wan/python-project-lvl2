# -*- coding:utf-8 -*-

"""Module with main function."""

from gendiff.formatters.jsonify_formatter import jsonify  # noqa: F401
from gendiff.formatters.plain_formatter import plain  # noqa: F401
from gendiff.formatters.stylish_formatter import stylish
from gendiff.modules.abstract_for_gendiff import gen_diff_dict
from gendiff.modules.parsing_data import parser


def generate_diff(first_file, second_file, formatter='stylish'):  # noqa: WPS210
    """Determine the difference of 2 json files.

    Args:
        formatter: function
        first_file: dict
        second_file: dict

    Returns:
        string with difference: str
    """
    formatters = {'plain': plain, 'stylish': stylish, 'json': jsonify}
    formatter = formatters.get(formatter)
    dictionary1 = parser(first_file)
    dictionary2 = parser(second_file)
    dict_with_changes = gen_diff_dict(dictionary1, dictionary2)
    return formatter(dict_with_changes)
