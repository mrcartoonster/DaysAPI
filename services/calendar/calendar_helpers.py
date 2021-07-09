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
    td = p.parse(dt[0].isoformat(), tz=tz)
    ft = td.add(
        years=years,
        months=months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )
    return ft.to_datetime_string()


def differ(first_date: str, sec_date: str, tz1: str = "UTC", tz2: str = "UTC"):
    if tz1 not in timezones or tz2 not in timezones:
        return "Cannot locate timezones."

    fd = list(df.find_dates(first_date))
    sd = list(df.find_dates(sec_date))

    if fd == [] or sd == []:
        return []

    fp = p.parse(fd[0].isoformat(), tz=tz1)
    sp = p.parse(sd[0].isoformat(), tz=tz2)

    diff_dict = {
        "time_zone_one": tz1,
        "time_zone_two": tz2,
        "years": fp.diff(sp).in_years(),
        "months": fp.diff(sp).in_months(),
        "weeks": fp.diff(sp).in_weeks(),
        "days": fp.diff(sp).in_days(),
        "hours": fp.diff(sp).in_hours(),
        "minutes": fp.diff(sp).in_minutes(),
        "seconds": fp.diff(sp).in_seconds(),
        "words": fp.diff(sp).in_words(),
    }

    return diff_dict


def isoformatter(the_date: str, tz: str = "UTC") -> str:
    """
    This function will return properly formatted date.
    """
    fd = list(df.find_dates(the_date))
    fp = p.parse(fd[0].isoformat(), tz=tz)

    return fp.to_iso8601_string()
