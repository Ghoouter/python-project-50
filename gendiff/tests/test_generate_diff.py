import pytest

from gendiff.modules.generate_diff import generate_diff


@pytest.fixture
def file1_json():
	return "gendiff/tests/fixtures/file1.json"


@pytest.fixture
def file2_json():
	return "gendiff/tests/fixtures/file2.json"


@pytest.fixture
def file1_yaml():
	return "gendiff/tests/fixtures/file1.yaml"


@pytest.fixture
def file2_yaml():
	return "gendiff/tests/fixtures/file2.yaml"


def test_generate_diff_json(file1_json, file2_json):
	expected_diff = """\
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true"""
	assert generate_diff(file1_json, file2_json) == expected_diff


def test_generate_diff_yaml(file1_yaml, file2_yaml):
	expected_diff = """\
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true"""
	assert generate_diff(file1_yaml, file2_yaml) == expected_diff