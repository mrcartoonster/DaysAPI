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
    test_date = working_days("02-02-21", 5)
    assert test_date == "Thursday, February 28 2002"


def test_delta_working_days_helper_function_passing():
    """
    Passing delta working days.
    """
    test_date = delta_working("12-13-2012", "01-18-2013")
    assert test_date == (
        "There are 24 business days between Thursday, December 13 2012"
        " and Friday, January 18 2013."
    )


def test_holiday_list_passing(holidaysdict):
    """
    Confirm holidays is returned correctly.
    """
    assert holidays() == holidaysdict
