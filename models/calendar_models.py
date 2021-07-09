# -*- coding: utf-8 -*-
# Response models for Calendar endpoints
import pendulum as p
from pydantic import BaseModel, Field


class Arithmetic(BaseModel):
    """
    Response model for arithmetic endpoint.
    """

    date_entered: str = Field(
        default=p.now().to_day_datetime_string(),
        description="Date enterd to count days from",
    )
    tz: str = Field(
        default="UTC",
        title="Time Zone",
        description="Selected Time Zone.",
    )
    years: int = Field(default=0, description="Number of years")
    months: int = Field(default=0, description="Number of months")
    days: int = Field(default=8, description="Number of days")
    hours: int = Field(default=0, description="Number of hours")
    minutes: int = Field(default=0, description="Number of minutes")
    seconds: int = Field(default=0, description="Number of seconds")
    returned_date: str = Field(
        default=p.now().add(days=8).to_iso8601_string(),
        description="Returned date after calculation",
    )


class PeriodOne(BaseModel):
    """
    First entered date.
    """

    date_one: str = Field(
        p.now().to_datetime_string(),
        title="Date One",
        description="First date entered",
    )
    formatted_date_one: str = Field(
        p.now().to_iso8601_string(),
        title="Date One formatted",
        description="Date One entered formatted in ISO-8601 format",
    )


class PeriodTwo(BaseModel):
    """
    Second entered date.
    """

    date_two: str = Field(
        p.now().add(months=2).to_datetime_string(),
        title="Date Two",
        description="Second date entred",
    )
    formatted_date_two: str = Field(
        p.now().add(months=2).to_iso8601_string(),
        title="Date two formatted",
        description="Date entered formatted in ISO-8601 format",
    )


class Difference(BaseModel):
    """
    Response model for datetime difference calculation.
    """

    time_zone_one: str = Field(
        default="UTC",
        description="Time zone for date one.",
    )
    time_zone_two: str = Field(
        default="UTC",
        description="Time zone for date two.",
    )
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
