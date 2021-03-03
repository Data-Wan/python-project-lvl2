# -*- coding:utf-8 -*-

"""Help documentation."""
from gendiff.cli import take_args
from gendiff.gendiff import generate_diff

args = take_args()


def main():
    """Print generate diff for 2 json files."""
    try:
        print(generate_diff(args.first_file, args.second_file, args.format))
    except TypeError:
        print('Oops!  That was no valid input.  Try again...')


if __name__ == '__main__':
    main()
