# -*- coding:utf-8 -*-

"""Module with argparse."""
import argparse


def take_args():
    """Pars arguments.

    Returns:
        arguments: any
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')  # noqa: E501
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    return parser.parse_args()
