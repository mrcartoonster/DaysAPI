# -*- coding: utf-8 -*-
# Location of fixtures and variables
import pytest

holiday_dict = {
    "Friday, January 01 2021": "New year",
    "Monday, January 18 2021": "Birthday of Martin Luther King, Jr.",
    "Monday, February 15 2021": "Washington's Birthday",
    "Monday, May 31 2021": "Memorial Day",
    "Sunday, July 04 2021": "Independence Day",
    "Monday, July 05 2021": "Independence Day (Observed)",
    "Monday, September 06 2021": "Labor Day",
    "Monday, October 11 2021": "Columbus Day",
    "Thursday, November 11 2021": "Veterans Day",
    "Thursday, November 25 2021": "Thanksgiving Day",
    "Friday, December 24 2021": "Christmas Day (Observed)",
    "Saturday, December 25 2021": "Christmas Day",
    "Friday, December 31 2021": "New Years Day (Observed)",
}


@pytest.fixture()
def holidaysdict():
    """
    Returns a diction of properly date formated dictionary of US federal
    holidays.
    """
    return holiday_dict
