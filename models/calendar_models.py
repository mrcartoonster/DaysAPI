# -*- coding: utf-8 -*-
# Response models for Calendar endpoints
import pendulum as p
from pydantic import BaseModel


class Arithmetic(BaseModel):
    """
    Response model for arithmetic endpoint.
    """

    date_entered: str = p.now().to_day_datetime_string()
    tz: str = "UTC"
    years: int = 0
    months: int = 0
    days: int = 8
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    returned_date: str = p.now().add(days=8).to_day_datetime_string()


class PeriodOne(BaseModel):
    """
    First entered date.
    """

    date_one: str = p.now().to_date_string()


class PeriodTwo(BaseModel):
    """
    Second entered date.
    """

    date_two: str = p.now().add(months=2).to_date_string()


class Difference(BaseModel):
    """
    Response model for datetime difference calculation.
    """

    time_zone: str = "UTC"
    years: int = 0
    months: int = 0
    weeks: int = 0
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    words: str = "4 years 3 months 2 weeks and 1 day til' I'm out!"


class Diff(BaseModel):
    """
    Response Model for Difference endpoint.
    """

    period_one: PeriodOne
    period_two: PeriodTwo
    difference: Difference
