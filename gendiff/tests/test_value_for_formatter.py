from gendiff.formatters.stylish import stylish_value
from gendiff.formatters.plain import plain_value
from gendiff.formatters.json import json_value


def test_stylish_value():
    assert stylish_value(False, 0) == 'false'
    assert stylish_value(None, 0) == 'null'
    assert stylish_value(5, 0) == '5'


def test_stylish_value_for_dict(file1):
    with open('gendiff/tests/fixtures/stylish_value_result.txt') as f:
        assert stylish_value(file1, 0) == f.read()


def test_plain_value(file1):
    assert plain_value(file1) == '[complex value]'
    assert plain_value(True) == 'true'
    assert plain_value(False) == 'false'
    assert plain_value(None) == 'null'
    assert plain_value('bar') == "'bar'"


def test_json_value(file1):
    assert json_value(5) == 5
    assert json_value('') is None
    assert json_value(file1) == {'a': 'hexlet', 'b': True, 'c': 234}