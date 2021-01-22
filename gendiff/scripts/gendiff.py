# -*- coding:utf-8 -*-

"""Help documentation"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help="set format of output")
parser.parse_args()
