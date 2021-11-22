#!/usr/bin/env python

"""Tests for `file_processor` package."""
import sys
sys.path.append('.')
import pytest
from file_processor.utils.helpers import validate_iso8601_utc, filter_json_date

# @pytest.fixture
def test_utc_validator():

    assert validate_iso8601_utc('2000-01-06T06:27:36Z') is True

    assert validate_iso8601_utc('2000-01-54T06:27:36Z') is False

    assert validate_iso8601_utc('2000-01-06T06:27:36Z.06') is False


def test_file_processor():

    file_name = 'test_data/sample1.txt'
    start_datetime= '2000-01-01T17:25:49Z'
    end_datetime = '2000-01-06T06:27:36Z'

    try:
        response = filter_json_date(file_name, start_datetime, end_datetime)
        f = True
    except:
        f=False

    assert f is True


