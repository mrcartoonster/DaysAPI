# -*- coding: utf-8 -*-
from services.business.working_helpers import (
    delta_working,
    holidays,
    working_days,
)


def test_working_days_helper_function_passing():
    """
    Passing working days function.
    """
    test_date = working_days("2021-06-29", 8)
    assert test_date == "2021-07-12"


def test_delta_working_days_helper_function_passing():
    """
    Passing delta working days.
    """
    test_date = delta_working("2020-06-20", "2020-07-21")
    assert test_date == 21


def test_holiday_list_passing(holidaysdict):
    """
    Confirm holidays is returned correctly.
    """
    assert holidays() == holidaysdict
