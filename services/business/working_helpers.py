# -*- coding: utf-8 -*-
# Addworking days func
import datefinder as df
import pendulum as p
from workalendar.usa import UnitedStates

us = UnitedStates()

dt_fmt = "%A, %B %d %Y"


def working_days(
    date: str = p.now().to_date_string(),
    days: int = 8,
) -> str:
    """
    Add working days function.
    """
    dt = list(df.find_dates(date))
    if dt == []:
        return []
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
    if fd == []:
        return []
    sd = list(df.find_dates(second_date))
    if sd == []:
        return []
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
