# -*- coding: utf-8 -*-
# Addworking days func
import pendulum as p
from workalendar.usa import UnitedStates

cal = UnitedStates()

date_fmt = "dddd, MMMM DD YYYY"


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
    return from_day.format(fmt=date_fmt)


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
    working_date = (
        f"There are {num_days} business days between "
        f"{f_day.format(fmt=date_fmt)} and {s_day.format(fmt=date_fmt)}."
    )
    return working_date
