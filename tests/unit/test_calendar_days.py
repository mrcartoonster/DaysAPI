# -*- coding: utf-8 -*-
# Test for calenddar function helpers
from services.calendar.calendar_helpers import arithmetic, differ


def test_arithmetic_add_passing():
    """
    Test helper addition functionality.
    """
    test_date = arithmetic(date="1-1-21")
    assert test_date == "2021-01-09 00:00:00"


def test_arithmetic_subtraction_passing():
    """
    Test helper for subtraction default.
    """
    test_date = arithmetic(date="1-1-21", days=-8)
    assert test_date == "2020-12-24 00:00:00"


def test_arithmetic_tz_failing():
    """
    Confirm that when an incorrect timezone is entered, you get the
    error printed.
    """
    test_date = arithmetic("1-1-21", tz="US/North")
    assert test_date == "US/North is not a timezone we have on file."


def test_arithmetic_datetime_failing():
    """
    Confirm that when incorrect or malformed date is entered, an error
    is given.

    An error will not be given. an empty list: `[]` will given so
    FastAPI's HTTPException will be able to catch it.

    """
    test_date = arithmetic("2, j 2011")
    assert test_date == []


def test_differ_passing():
    """
    Ensure passing when 2 valid dates are entered.
    """
    test_dates = differ("01-22-2021", "03-02-2023")
    assert test_dates == {
        "tz": "UTC",
        "years": 2,
        "months": 25,
        "weeks": 109,
        "days": 769,
        "hours": 18456,
        "minutes": 1107360,
        "seconds": 66441600,
        "words": "2 years 1 month 1 week 1 day",
    }


def test_differ_failing():
    """
    Ensure None is returned when date cannot be parsed.
    """
    test_dates = differ("2 j 2021", "03-03-2023")
    assert test_dates == []
