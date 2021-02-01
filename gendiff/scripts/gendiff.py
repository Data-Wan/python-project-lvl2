# -*- coding:utf-8 -*-

"""Help documentation."""

import argparse

from gendiff.gendiff import generate_diff

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', default='stylish', help='set format of output')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

args = parser.parse_args()


def main():
    """Print generate diff for 2 json files."""
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
