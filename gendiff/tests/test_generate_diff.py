import pytest

from gendiff import generate_diff

parameter = [('path1_json', 'path2_json', 'stylish', 'gendiff/tests/fixtures/result_stylish.txt'),
             ('path1_json', 'path2_json', 'plain', 'gendiff/tests/fixtures/result_plain.txt'),
             ('path1_json', 'path2_json', 'json', 'gendiff/tests/fixtures/result_json.txt'),
             ('path1_yaml', 'path2_yaml', 'stylish', 'gendiff/tests/fixtures/result_stylish.txt'),
             ('path1_yaml', 'path2_yaml', 'plain', 'gendiff/tests/fixtures/result_plain.txt'),
             ('path1_yaml', 'path2_yaml', 'json', 'gendiff/tests/fixtures/result_json.txt')]


@pytest.mark.parametrize("path1, path2, format, expected", parameter)
def test_generate_diff(path1, path2, format, expected, request):
    path1 = request.getfixturevalue(path1)
    path2 = request.getfixturevalue(path2)
    with open(expected) as result:
        assert generate_diff(path1, path2, format) == result.read()