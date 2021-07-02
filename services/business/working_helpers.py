# -*- coding: utf-8 -*-
# Addworking days func
import pendulum as p
from workalendar.usa import UnitedStates

cal = UnitedStates()

# Pendulum date formatting
date_fmt = "dddd, MMMM-DD-YYYY"

# datetime date formatting
dt_fmt = "%A, %B %d %Y"


def working_days(
    first_date: str = p.now().to_date_string(),
    num: int = 8,
) -> str:
    """
    Add working days function.
    """
    day = p.parse(first_date, strict=False)
    the_day = cal.add_working_days(day, num)
    from_day = p.parse(str(the_day))
    return from_day.to_date_string()


def delta_working(
    first_date: str,
    second_date: str,
):
    """
    Function will return number of business days between to dates given.
    """
    f_day = p.parse(first_date, strict=False)
    s_day = p.parse(second_date, strict=False)
    num_days = cal.get_working_days_delta(start=f_day, end=s_day)
    return num_days


def holidays(year: int = p.now().year):
    """
    Helper function to return properly formatted holiday dates.
    """
    holiday_list = cal.holidays(year)
    holiday_formatted = {
        key.strftime(dt_fmt): value for key, value in holiday_list
    }
    return holiday_formatted