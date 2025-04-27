import pytest

from gendiff import generate_diff


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










