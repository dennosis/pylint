# pylint: disable=missing-module-docstring,missing-function-docstring,wrong-import-position
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from text import find_substring_by_regex


@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("abc123def456", r"\d+", "123"),
        ("hello world", r"o\w+", "orld"),
        ("no match here", r"\d+", None),
        ("aaa bbb ccc", r"a+", "aaa"),
        ("", r".+", None),
    ],
)
def test_find_substring_by_regex(text, pattern, expected):
    assert find_substring_by_regex(text, pattern) == expected
