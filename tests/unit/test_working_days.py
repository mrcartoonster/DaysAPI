# -*- coding: utf-8 -*-
from services.business.add_working import working_days


def test_working_days_helper_function_passing():
    """
    Passing working days function.
    """
    test_date = working_days("02-02-21", 5)
    assert test_date == "Thursday, February 28 2002"
