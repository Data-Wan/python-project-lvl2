# -*- coding:utf-8 -*-

"""Project 2."""

from gendiff.formatters.jsonify import jsonify
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

all_formatters = {
    'plain': plain,
    'stylish': stylish,
    'json': jsonify,
}
