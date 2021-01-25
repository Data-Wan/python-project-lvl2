# -*- coding:utf-8 -*-

"""Help documentation."""

import argparse

from calculate_diff.modules.generate_gendiff import generate_diff

parser = argparse.ArgumentParser()
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()

if __name__ == '__main__':
    print(generate_diff(args.first_file, args.second_file))
