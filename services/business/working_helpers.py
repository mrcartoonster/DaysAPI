# -*- coding: utf-8 -*-
# Addworking days func
from typing import Union

import datefinder as df
import pendulum as p
from workalendar.usa import UnitedStates

us = UnitedStates()

dt_fmt = "%A, %B %d %Y"


def working_days(
    date: str = p.now().to_date_string(),
    days: int = 8,
) -> Union[str, None]:
    """
    Add working days function.
    """
    dt = list(df.find_dates(date))
    if dt:
        td = p.parse(dt[0].isoformat(), tz="US/Eastern")
        bus_date = us.add_working_days(td, days)
        return bus_date.to_date_string()


def delta_working(
    first_date: str,
    second_date: str,
):
    """
    Function will return number of business days between to dates given.
    """
    fd = list(df.find_dates(first_date))
    sd = list(df.find_dates(second_date))

    if fd and sd:
        fp = p.parse(fd[0].isoformat())
        sp = p.parse(sd[0].isoformat())
        num_days = us.get_working_days_delta(start=fp, end=sp)
        return num_days


def holidays(year: int = p.now().year):
    """
    Helper function to return properly formatted holiday dates.
    """
    holiday_list = us.holidays(year)
    holiday_formatted = {
        key.strftime(dt_fmt): value for key, value in holiday_list
    }
    return holiday_formatted


def to_day_string(the_date: str):
    """
    Helper function to return human readable date.
    """
    fd = list(df.find_dates(the_date))
    fp = p.parse(fd[0].isoformat())

    return fp.to_cookie_string()
