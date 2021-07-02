# -*- coding: utf-8 -*-
import datefinder as df
import pendulum as p
from pendulum import timezones


def daterng(start: str, end: str):
    """
    Creates a list of dates between start (inclusive) and end (not
    inclusive).
    """
    s = p.parse(start, strict=False)
    e = p.parse(end, strict=False)
    duration = [s + p.duration(_) for _ in range(int((e - s).days))]
    return [_.format("dddd, MM-DD-YYYY") for _ in duration]


def arithmetic(
    date: str,
    tz: str = "UTC",
    years: int = 0,
    months: int = 0,
    days: int = 8,
    hours: int = 0,
    minutes: int = 0,
    seconds: int = 0,
) -> str:
    if tz not in timezones:
        return f"{tz} is not a timezone we have on file."

    dt = list(df.find_dates(date))
    if dt == []:
        return []
    td = p.parse(dt[0].isoformat())
    ft = td.add(
        years=years,
        months=months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )
    return ft.to_datetime_string()
