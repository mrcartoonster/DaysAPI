# -*- coding: utf-8 -*-
from services.business.working_delta import delta_working


def test_delta_working_days_helper_function_passing():
    """
    Passing delta working days.
    """
    test_date = delta_working("12-13-2012", "01-18-2013", 24)
    assert test_date == (
        "The number of business days between Thursday, December 13 2013"
        " and Friday, January 18 2013 is 24."
    )
