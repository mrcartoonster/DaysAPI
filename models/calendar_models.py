# -*- coding: utf-8 -*-
# Response models for Calendar endpoints
from enum import Enum

import pendulum as p
from pydantic import BaseModel, Field


class Arithmetic(BaseModel):
    """
    JSON Schema Response model for arithmetic endpoint.
    """

    date_entered: str = Field(
        default=p.now().to_day_datetime_string(),
        description="Date enterd to count days from.",
    )
    tz: str = Field(
        default="UTC",
        title="Time Zone",
        description="Selected Time Zone.",
    )
    years: int = Field(default=0, description="Number of years.")
    months: int = Field(default=0, description="Number of months.")
    days: int = Field(default=8, description="Number of days.")
    hours: int = Field(default=0, description="Number of hours.")
    minutes: int = Field(default=0, description="Number of minutes.")
    seconds: int = Field(default=0, description="Number of seconds.")
    returned_date: str = Field(
        default=p.now().add(days=8).to_iso8601_string(),
        description="Returned date after calculation.",
    )


class PeriodOne(BaseModel):
    """
    JSON Schema Response model for first entered date.
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
    JSON Schema Response Mode for second date entered.
    """

    date_two: str = Field(
        p.now().add(months=2).to_datetime_string(),
        title="Date Two",
        description="Second date entred",
    )
    formatted_date_two: str = Field(
        p.now().add(months=2).to_iso8601_string(),
        title="Date two formatted",
        description="Date entered formatted in ISO-8601 format.",
    )


class Difference(BaseModel):
    """
    JSON Schema Response model for datetime difference calculation.
    """

    time_zone_one: str = Field(
        default="UTC",
        description="Time zone for date one.",
    )
    time_zone_two: str = Field(
        default="UTC",
        description="Time zone for date two.",
    )
    years: int = Field(default=0, description="Number of years.")
    months: int = Field(default=0, description="Number of months.")
    weeks: int = Field(
        default=0,
        description="Number of weeks.",
    )
    days: int = Field(default=0, description="Number of days.")
    hours: int = Field(
        default=0,
        description="Number of hours.",
    )
    minutes: int = Field(default=0, description="Number of minutes.")
    seconds: int = Field(default=0, description="Number of seconds.")
    words: str = Field(
        default="4 years 3 months 2 weeks and 1 day til' I'm out!",
        description="Calculation in human readable form.",
    )


class Diff(BaseModel):
    """
    JSON Schema Response Model for Difference endpoint.
    """

    period_one: PeriodOne
    period_two: PeriodTwo
    difference: Difference


class WeekDay(BaseModel):
    """
    JSON Schema Response Model for is_weekday endpoint.
    """

    date_entered: str = Field(
        default=p.now().to_date_string(),
        description="Entered format of datestring.",
    )
    isoformat: str = Field(
        default=p.now().to_iso8601_string(),
        description="ISO-8601 format of datestring",
    )
    is_weekday: bool = Field(
        default=True,
        description=("True if date is a weekday: Monday through Friday."),
    )
    day_of_week: str = Field(
        default="Monday",
        description="Day of week name of date entered.",
    )


class WeekEnd(BaseModel):
    """
<<<<<<< HEAD
    JSON Schema Response Model for is_weeknd endpoint.
=======
    JSON Schema Response Model for is_weekend endpoint.
>>>>>>> DR-13-thirteenth
    """

    date_entered: str = Field(
        default=p.now().to_date_string(),
<<<<<<< HEAD
        description="Entered format of datestring.",
    )
    isoformat: str = Field(
        default=p.now().to_iso8601_string(),
        description="ISO-8601 format of datestring.",
    )
    is_weekend: bool = Field(
        default=True,
        description="True if date entered is Saturday or Sunday.",
    )
    day_of_week: str = Field(
        default="Monday",
        description="Day name of date entered.",
    )
=======
        description="Entered formatted date of datestring.",
    )
    isoformat: str = Field(
        default=p.now().to_iso8601_string(),
        description=("Date in ISO-8601 format."),
    )
    is_weekend: bool = Field(
        default=True,
        description="True if date given falls on Saturday or Sunday.",
    )
    day_of_week: str = Field(
        default="Saturday",
        description="Day of weekday named entered.",
    )


class DateForm(str, Enum):
    """
    This is an enumartion of date formats.
    """

    atom_string = "atom_string"
    cookie_string = "cookie_string"
    iso_8601 = "iso_8601"
    rfc_822 = "rfc_822"
    rfc_850 = "rfc_850"
    rfc_1036 = "rfc_1036"
    rfc_1123 = "rfc_1123"
    rfc_2822 = "rfc_2822"
    rfc_3339 = "rfc_3339"
    rss = "rss"
    w3c = "w3c"


class FormatRequest(BaseModel):
    """
    Request Body for POST for date_format endpoint.
    """

    dateform: DateForm = Field(
        default=DateForm.iso_8601,
        description="Date Form selected. Default is ISO-8601",
    )
    dates: str = Field(
        default=p.now().to_iso8601_string(),
        description="Formatted list of entered date or dates.",
    )
    time_zone: str = Field(default="UTC", description="Selected time zone.")


class FormatResponse(BaseModel):
    """
    JSON Schema for date format Response model.
    """

    entered_dates: str = Field(
        default="",
        description="Entered dates or date.",
    )
    format_selection: str = Field(
        default="cookie_string",
        description="Format date string selected. Default is ISO-8601.",
    )
    formatted_list: list[str] = Field(
        default=[p.now().to_date_string()],
        description="Return of formatted date or dates.",
    )
    time_zone: str = Field(default="UTC", description="Selected timezone")
>>>>>>> DR-13-thirteenth
