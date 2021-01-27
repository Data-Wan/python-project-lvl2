"""File for test gendiff."""
from calculate_diff.modules.generate_gendiff import generate_diff


def test_flat_files():
    with open('tests/fixtures/check_for_f1_f2.txt') as example:
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == example.read()
