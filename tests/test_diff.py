"""File for test gendiff."""
import json
import pytest

from gendiff.gendiff import generate_diff


@pytest.mark.parametrize("first_file_path, "
                         "second_file_path, "
                         "result_path",
                         [
                             ('tests/fixtures/file1.json',
                              'tests/fixtures/file2.json',
                              'tests/fixtures/result_for_test_flate.txt'),

                             ('tests/fixtures/yaml_file1.yml',
                              'tests/fixtures/yaml_file2.yml',
                              'tests/fixtures/result_for_test_flate.txt'),

                             ('tests/fixtures/nested_file1.json',
                              'tests/fixtures/nested_file2.json',
                              'tests/fixtures/result_for_test_nested.txt'),

                             ('tests/fixtures/nested_yaml_file1.yml',
                              'tests/fixtures/nested_yaml_file2.yml',
                              'tests/fixtures/result_for_test_nested.txt')
                         ])
def test_default_output(first_file_path, second_file_path, result_path):
    with open(result_path) as example:
        input_data = generate_diff(first_file_path, second_file_path)
        result = example.read()
        assert input_data == result


@pytest.mark.parametrize("first_file_path, second_file_path",
                         [
                             ('tests/fixtures/nested_file1.json',
                              'tests/fixtures/nested_file2.json'),

                             ('tests/fixtures/nested_yaml_file1.yml',
                              'tests/fixtures/nested_yaml_file2.yml')
                         ])
@pytest.mark.parametrize("result_path, format_out",
                         [
                             ('tests/fixtures/result_for_plain.txt',
                              'plain')
                         ])  # plain output
def test_formatted_output(first_file_path, second_file_path, format_out, result_path):
    with open(result_path) as example:
        input_data = generate_diff(first_file_path, second_file_path, format_out)
        result = example.read()
        assert input_data == result


@pytest.mark.parametrize("first_file_path, second_file_path",
                         [
                             ('tests/fixtures/nested_file1.json',
                              'tests/fixtures/nested_file2.json'),

                             ('tests/fixtures/nested_yaml_file1.yml',
                              'tests/fixtures/nested_yaml_file2.yml')
                         ])
@pytest.mark.parametrize("result_path, format_out",
                         [
                             ('tests/fixtures/result_for_jsonify.json',
                              'json')
                         ])  # json output
def test_jsonify_output(first_file_path, second_file_path, format_out, result_path):
    with open(result_path) as example:
        input_data = json.loads(generate_diff(first_file_path, second_file_path,
                                              format_out))
        result = json.load(example)
        assert input_data == result
