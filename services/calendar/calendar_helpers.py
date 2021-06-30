# -*- coding: utf-8 -*-
import pendulum as p


def daterng(start: str, end: str):
    """
    Creates a list of dates between start (inclusive) and end (not
    inclusive).
    """
    s = p.parse(start, strict=False)
    e = p.parse(end, strict=False)
    duration = [s + p.duration(_) for _ in range(int((e - s).days))]
    return [_.format("dddd, MM-DD-YYYY") for _ in duration]


def days_ago(day: str = p.now().to_date_string(), num: int = 8):
    """
    Days ago helper function.

    Takes date and subtracts and outputs date string.

    """
    if day is not None:
        the_day = p.parse(day, strict=False)
        ago = the_day - p.duration(num)
    else:
        day = p.today()
        ago = day - p.duration(num)

    return ago.to_date_string()
