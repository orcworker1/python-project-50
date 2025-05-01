import pytest

from gendiff import generate_diff
from gendiff.formatters.plain import format_plain


@pytest.fixture
def nested_json1():
    return 'tests/fixture/nested1.json'


@pytest.fixture
def nested_json2():
    return 'tests/fixture/nested2.json'


@pytest.fixture
def nested_yaml1():
    return 'tests/fixture/nested1.yaml'


@pytest.fixture
def data_1():
    return 'tests/fixture/file1.json'


@pytest.fixture
def data_2():
    return 'tests/fixture/file2.json'


@pytest.fixture
def data_yaml_1():
    return 'tests/fixture/file1.yaml'


@pytest.fixture
def data_yaml_2():
    return 'tests/fixture/file2.yaml'


@pytest.fixture
def sample_diff():
    return {
        'common': {
            'type': 'nested',
            'children': {
                'follow': {'type': 'added', 'value': False},
                'setting2': {'type': 'removed', 'value': 200},
                'setting3': {
                    'type': 'changed',
                    'old': True,
                    'new': None
                }
            }
        }
    }


def test_nested_diff(nested_json1, nested_json2):
    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert generate_diff(nested_json1, nested_json2) == expected


def test_flat_yaml_diff(data_yaml_1, data_yaml_2):
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(data_yaml_1, data_yaml_2) == expected


def test_mixed_files(data_1, data_yaml_2):
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(data_1, data_yaml_2) == expected


def test_flat_json_diff(data_1, data_2):
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(data_1, data_2) == expected


def test_parse_file(data_1):
    assert generate_diff(data_1, data_1) == """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""


def test_plain_format(sample_diff):
    expected = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null"""
    assert format_plain(sample_diff) == expected