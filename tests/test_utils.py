# -*- coding: utf-8 -*-
import io
import json
import os
import tempfile
from pathlib import Path

import pytest
from slack_time.utils import comma_separated_string
from slack_time.utils import make_file
from slack_time.utils import make_json_encoded

FILENAME = "hello.txt"
TEXT = "Hello World!"


@pytest.fixture
def temp_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir) / FILENAME
        with open(str(temp_file), "w+") as f:
            f.write(TEXT)

        os.chdir(temp_dir)
        yield temp_file


def test_make_file_with_str(temp_file):
    f = make_file(FILENAME)
    assert isinstance(f, io.BufferedReader)
    assert f.read().decode() == TEXT


def test_make_file_with_os_pathlike(temp_file):
    f = make_file(temp_file)
    assert isinstance(f, io.BufferedReader)
    assert f.read().decode() == TEXT


def test_make_file_with_io(temp_file):
    f = make_file(open(temp_file, "rb"))
    assert isinstance(f, io.BufferedReader)
    assert f.read().decode() == TEXT


@pytest.mark.parametrize("field", [[1, 2, 3], {1: "a", 2: "b"}])
def test_make_json_encoded(field):
    assert make_json_encoded(field) == json.dumps(field)


def test_make_json_encoded_str():
    assert make_json_encoded("hello") == "hello"


@pytest.mark.parametrize("field", [1, 1.2, (1, 2), {1, 2}, True, b"hello"])
def test_make_json_encoded_fails(field):
    with pytest.raises(TypeError):
        make_json_encoded(field)


@pytest.mark.parametrize("string", ["hello", "hello,goodbye"])
def test_comma_separated_string(string):
    assert comma_separated_string(string) == string


@pytest.mark.parametrize(
    "iterable", [("a", "b"), ["a", "b"], {"a", "b"}, {"a": "b"}]
)
def test_comma_separated_string_with_iterable(iterable):
    assert comma_separated_string(iterable) == ",".join(iterable)
