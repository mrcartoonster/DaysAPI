# -*- coding: utf-8 -*-
# Response models for Calendar endpoints
import pendulum as p
from pydantic import BaseModel, Field


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
    returned_date: str = p.now().add(days=8).to_iso8601_string()


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
