# -*- coding:utf-8 -*-

"""Help documentation."""

import argparse

from gendiff.gendiff import generate_diff
from gendiff.modules.jsonify_formatter import jsonify  # noqa: F401
from gendiff.modules.plain_formatter import plain  # noqa: F401
from gendiff.modules.stylish_formatter import stylish

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', default=stylish, help='set format of output')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

args = parser.parse_args()
formatters = {'plain': plain, 'stylish': stylish, 'json': jsonify}


def main():
    """Print generate diff for 2 json files."""
    format_to_call = formatters[args.format]
    print(generate_diff(args.first_file, args.second_file, format_to_call))


if __name__ == '__main__':
    main()
