# -*- coding: utf-8 -*-
# Test for calenddar function helpers
from services.calendar.calendar_helpers import days_ago


def test_days_ago():
    """
    This will test the days ago helper function.
    """
    test_date = days_ago("2020-02-21", 5)
    assert test_date == "2020-02-16"
