"""File for test gendiff."""
import json

from calculate_diff.modules.generate_diff import generate_diff, gen_diff_dict
from calculate_diff.modules.jsonify_formatter import jsonify
from calculate_diff.modules.plain_formatter import plain


def test_flat_files():
    with open('tests/fixtures/result_for_test_flate.txt') as example:
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == example.read()
        example.seek(0)
        assert generate_diff('tests/fixtures/yaml_file1.yml', 'tests/fixtures/yaml_file2.yml') == example.read()


def test_nested_files():
    with open('tests/fixtures/result_for_test_nested.txt') as example:
        assert generate_diff('tests/fixtures/nested_file1.json', 'tests/fixtures/nested_file2.json') == example.read()
        example.seek(0)
        assert generate_diff('tests/fixtures/nested_yaml_file1.yml',
                             'tests/fixtures/nested_yaml_file2.yml') == example.read()


def test_plain_output():
    with open('tests/fixtures/result_for_plain.txt') as example:
        a = generate_diff('tests/fixtures/nested_file1.json', 'tests/fixtures/nested_file2.json', plain)
        b = example.read()
        assert a == b
        example.seek(0)
        assert generate_diff('tests/fixtures/nested_yaml_file1.yml', 'tests/fixtures/nested_yaml_file2.yml',
                             plain) == example.read()


def test_jsonify_output():
    with open('tests/fixtures/result_for_jsonify.json') as example:
        assert json.loads(generate_diff('tests/fixtures/nested_file1.json', 'tests/fixtures/nested_file2.json',
                                        jsonify)) == json.load(example)