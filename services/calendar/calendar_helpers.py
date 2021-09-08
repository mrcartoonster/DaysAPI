# -*- coding: utf-8 -*-
from typing import List, Union

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
) -> Union[str, None]:
    if tz not in timezones:
        return f"{tz} is not a timezone we have on file."

    dt = list(df.find_dates(date))
    if dt:
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

    if fd and sd:
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


def weekday(the_date: str) -> Union[str, None]:
    """
    Function that will return True/False to check if day is a weekday.
    """

    fd = list(df.find_dates(the_date))

    if fd:
        fp = p.parse(fd[0].isoformat())
        return fp.day_of_week not in [0, 6]


def weekend(the_date: str) -> Union[str, None]:
    """
    Helper function to output True/False to check if date given is a
    weekend.
    """

    fd = list(df.find_dates(the_date))

    if fd:
        fp = p.parse(fd[0].isoformat())
        return fp.day_of_week in [0, 6]


def day_of_week(date: str):
    """
    Quick function to output the day name of week.
    """
    fd = list(df.find_dates(date))

    if fd:
        return p.parse(fd[0].isoformat()).format("dddd")


# Format functions
def rfc_822(date: str, tz: str = "UTC") -> List[str]:
    """
    RFC-822 format.
    """
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_rfc822_string() for _ in fd]


def rfc_850(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_rfc850_string() for _ in fd]


def rss(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_rss_string() for _ in fd]


def w3c(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_w3c_string() for _ in fd]


def iso_8601(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_iso8601_string() for _ in fd]


def atom_string(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_atom_string() for _ in fd]


def cookie_string(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_cookie_string() for _ in fd]


def rfc_1036(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_rfc1036_string() for _ in fd]


def rfc_1123(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [p.parse(_.isoformat(), tz=tz).to_rfc1123_string() for _ in fd]


def rfc_2822(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [
        p.parse(_.isoformat(), tz=tz).to_rfc2822_string_string() for _ in fd
    ]


def rfc_3339(date: str, tz: str = "UTC") -> List[str]:
    d = date.replace(" ", " a ")
    fd = list(df.find_dates(d))
    return [
        p.parse(_.isoformat(), tz=tz).to_rfc3339_string_string_string()
        for _ in fd
    ]
