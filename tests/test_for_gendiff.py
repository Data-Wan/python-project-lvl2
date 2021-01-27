"""File for test gendiff."""
from calculate_diff.modules.generate_gendiff import generate_diff


def test_flat_files():
    with open('tests/fixtures/result_for_test.txt') as example:
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == example.read()
        example.seek(0)
        assert generate_diff('tests/fixtures/yaml_file1.yml', 'tests/fixtures/yaml_file2.yml') == example.read()
