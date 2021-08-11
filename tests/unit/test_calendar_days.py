# -*- coding: utf-8 -*-
# Test for calenddar function helpers
import pendulum as p
import pytest

from services.calendar.calendar_helpers import (
    arithmetic,
    differ,
    weekday,
    weekend,
)

# from hypothesis import given, strategies as st


@pytest.mark.parametrize("date", ["1-1-21"])
def test_arithmetic_add_passing(date):
    """
    Test helper addition functionality.
    """
    test_date = arithmetic(date=date)
    assert test_date == "2021-01-09 00:00:00"


def test_arithmetic_subtraction_passing():
    """
    Test helper for subtraction default.
    """
    test_date = arithmetic(date="1-1-21", days=-8)
    assert test_date == "2020-12-24 00:00:00"


def test_arithmetic_tz_failing(failed_days, failed_tz):
    """
    Confirm that when an incorrect timezone is entered, you get the
    error printed.
    """
    test_date = arithmetic(date=failed_days, tz=failed_tz)
    assert test_date == f"{failed_tz} is not a timezone we have on file."


def test_arithmetic_datetime_failing():
    """
    Confirm that when incorrect or malformed date is entered, an error
    is given.

    An error will not be given. an empty list: `[]` will given so
    FastAPI's HTTPException will be able to catch it.

    """
    test_date = arithmetic("2, j 22")
    assert test_date is None


def test_differ_passing():
    """
    Ensure passing when 2 valid dates are entered.
    """
    # We'll make fixtures later for this
    t1 = p.datetime(2021, 7, 12, 4, 22, tz="UTC")
    t2 = p.datetime(2021, 9, 6, 12, 13, tz="Pacific/Tahiti")

    test_dates = differ(
        first_date=t1.to_datetime_string(),
        sec_date=t2.to_datetime_string(),
        tz1="UTC",
        tz2="Pacific/Tahiti",
    )
    # We'll make this more robust with fixtures later on.
    assert t1.diff(t2).in_hours() in test_dates.values()
    assert (
        t1.timezone_name in test_dates.values()
        and t2.timezone_name in test_dates.values()
    )


def test_differ_failing():
    """
    Ensure None is returned when date cannot be parsed.
    """
    test_dates = differ("2 j 2021", "03-03-2023")
    assert test_dates is None


# Make a fixture for this to loop through know weekdays.
def test_weekday_passing():
    """
    Test that when given weekday True is outputted.
    """
    test_date = weekday("07-09-2021")
    assert test_date is True


def test_weekday_failing():
    """
    Test when date entered is badely formatted an empty list is
    returned.
    """
    test_date = weekday("2 j 22")
    assert test_date is None


def test_weekend_passing():
    """
    test functiono to ensure date pass when it's a weeknd.
    """
    test_date = weekend("07-11-21")
    assert test_date is True


def test_weekend_failing():
    """
    When an unparsable date's entered None is returned.
    """

    test_date = weekend("jul el 21")
    assert test_date is None
