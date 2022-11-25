from assertpy import assert_that
from jsonschema import validate
import json


def assert_contains(actual, expected):
    assert_that(actual).contains(expected)


def assert_field(actual, expected):
    assert_that(json.dumps(actual)).is_equal_to('"' + expected + '"')


def assert_not_null(value):
    assert_that(json.dumps(value)).is_not_empty()


def assert_status_code(actual, expected):
    assert_that(actual).is_equal_to(expected)


def assert_schema_response(actual, expected):
    validate(instance=actual, schema=expected)
