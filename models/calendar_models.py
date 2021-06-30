# -*- coding: utf-8 -*-
# Response models for Calendar endpoints
from pydantic import BaseModel


class DayAgo(BaseModel):
    """
    Response model for days_ago endpoint.
    """

    date: str
    days: int
    past_date: str
