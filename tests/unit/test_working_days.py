# -*- coding: utf-8 -*-
import pytest
from services.business.working_helpers import (
    delta_working,
    holidays,
    working_days,
)


def test_working_days_helper_function_passing(passing_days):
    """
    Passing working days function.
    """
    test_date = working_days(passing_days)
    assert test_date is not None


def test_working_days_helper_function_failing(wrong_days):
    """
    Test empty list is returned.
    """
    test_date = working_days(wrong_days)
    assert test_date is None


def test_delta_working_days_helper_function_passing():
    """
    Passing delta working days.
    """
    test_date = delta_working("2020-06-20", "2020-07-21")
    assert test_date == 21


# We'll update to use fixtuers for this.
def test_delta_working_days_helper_function_failing():
    """
    Test when incorrect date is entered that test fails.
    """
    test_date = delta_working("1 j 2021", "2-2-21")
    test_date2 = delta_working("1-1-21", "2 j 21")
    assert test_date is None
    assert test_date2 is None


def test_holiday_list_passing(holidaysdict):
    """
    Confirm holidays is returned correctly.
    """
    assert holidays() == holidaysdict
