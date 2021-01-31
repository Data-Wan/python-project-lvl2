# -*- coding:utf-8 -*-

"""Help documentation."""

import argparse

from calculate_diff.modules.generate_diff import generate_diff
from calculate_diff.modules.plain_formatter import plain  # noqa: F401
from calculate_diff.modules.stylish_funcs import stylish

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', default=stylish, help='set format of output')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

args = parser.parse_args()
formatters = {'plain': plain, 'stylish': stylish}


def main():
    """Print generate diff for 2 json files."""
    format_to_call = formatters[args.format]
    print(generate_diff(args.first_file, args.second_file, format_to_call))


if __name__ == '__main__':
    main()
