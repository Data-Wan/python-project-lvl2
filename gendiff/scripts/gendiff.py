# -*- coding:utf-8 -*-

"""Help documentation."""

import argparse
import json
from gendiff.scripts.stringify import stringify

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help="set format of output")
parser.parse_args()


def generate_diff(first_file, second_file):
    dictionary1 = json.load(open(first_file))
    dictionary2 = json.load(open(second_file))
    all_keys = union_keys(dictionary1, dictionary2)
    result = ['{', '}']
    for key in all_keys:
        result.insert(-1, '{0:>3d}'.format(key))















def union_keys(dictionary1, dictionary2):
    return set(dictionary1.keys()).union(set(dictionary2.keys()))
