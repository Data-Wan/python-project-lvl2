"""File for test gendiff."""
from calculate_diff.modules.generate_gendiff import generate_diff

example = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""


def test_flat_files():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == example
