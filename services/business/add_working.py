# -*- coding: utf-8 -*-
# Addworking days func
import pendulum as p
from workalendar.usa import UnitedStates

cal = UnitedStates()


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
    return from_day.format(fmt="dddd, MMMM DD YYYY")
