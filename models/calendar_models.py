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


class Difference(BaseModel):
    """
    Response model for datetime difference calculation.
    """

    ...
