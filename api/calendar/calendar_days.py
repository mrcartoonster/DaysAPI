# -*- coding: utf-8 -*-
import pendulum as p
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse

from models.calendar_models import DayAgo
from services.calendar.calendar_helpers import days_ago
from services.utilities.base import date_regex

router = APIRouter(
    prefix="/calendar",
    default_response_class=ORJSONResponse,
)


@router.get("/daysago", response_model=DayAgo)
async def daysago(
    date: str = Query(
        default=p.now().to_date_string(),
        description="Date to count back from",
    ),
    days: int = Query(default=8, description="Number of days to back from."),
):
    """
    Enter a date in YYYY-MM-DD or MM-DD-YYYY format as well a number to
    count back from date to get the date in calendar days.
    """
    if date_regex.search(date) is None:
        raise HTTPException(
            status_code=400,
            detail=(f"Date format: {date} is incorrect."),
        )
    ago = days_ago(date, days)
    return DayAgo(date=date, days=days, past_date=ago)
