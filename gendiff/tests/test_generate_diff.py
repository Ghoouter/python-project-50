import pytest

from gendiff.modules.generate_diff import generate_diff


@pytest.fixture
def file1():
	return "gendiff/tests/fixtures/file1.json"


@pytest.fixture
def file2():
	return"gendiff/tests/fixtures/file2.json"


def test_generate_diff(file1, file2):
	expected_diff = """\
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true"""
	assert generate_diff(file1, file2) == expected_diff