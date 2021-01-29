"""File for test gendiff."""
from calculate_diff.modules.generate_diff import generate_diff, gen_diff_dict


def test_flat_files():
    with open('tests/fixtures/result_for_test_flate.txt') as example:
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == example.read()
        example.seek(0)
        assert generate_diff('tests/fixtures/yaml_file1.yml', 'tests/fixtures/yaml_file2.yml') == example.read()


def test_nested_files():
    with open('tests/fixtures/result_for_test_nested.txt') as example:
        assert generate_diff('tests/fixtures/nested_file1.json', 'tests/fixtures/nested_file2.json') == example.read()
        example.seek(0)
        assert generate_diff('tests/fixtures/nested_yaml_file1.yml', 'tests/fixtures/nested_yaml_file2.yml') == example.read()
