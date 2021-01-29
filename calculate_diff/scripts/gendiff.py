# -*- coding:utf-8 -*-

"""Help documentation."""

import argparse

from calculate_diff.modules.generate_diff import generate_diff
from calculate_diff.modules.stulish_funcs import stylish

parser = argparse.ArgumentParser()
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default=stylish, help='set format of output')

args = parser.parse_args()


def main():
    """Print generate diff for 2 json files."""
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
