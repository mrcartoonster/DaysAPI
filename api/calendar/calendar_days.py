# -*- coding: utf-8 -*-
import pendulum as p
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse
from pendulum import timezones

from models.calendar_models import Arithmetic
from services.calendar.calendar_helpers import arithmetic

router = APIRouter(
    prefix="/calendar",
    default_response_class=ORJSONResponse,
)


# May use Depends on this. There's a lot of queries and a lot of lines
# of code.
@router.get("/arithmetic", response_model=Arithmetic)
async def daysago(
    date: str = Query(
        default=p.now().to_datetime_string(),
        description="Date for arithmetic calculation.",
    ),
    tz: str = Query(
        default="UTC",
        description=(
            "Time Zone. Timezone must be in"
            " [IANA](https://bit.ly/3h8wd73) format."
        ),
    ),
    years: int = Query(default=0, description="Number of years."),
    months: int = Query(default=0, description="Number of months"),
    days: int = Query(default=8, description="Number of days."),
    hours: int = Query(default=0, description="Number of hours."),
    minutes: int = Query(default=0, description="Number of minutes."),
    seconds: int = Query(default=0, description="number of seconds."),
):
    """
    This endpoint will take in a date and enter number of years, months,
    days, hours, minutes, and seconds as query parameters and return the
    date produced from said query parameters.

    If you want to go into the past, subtract from date and time enterd,
    add a `-`. For example, I want to go back 10 days I'll enter `-10`.
    If I want to go into the future 10 days then just enter 10. This goes
    for all other parameters to go back or forth in time.

    **Note**: Please enter properly formatted dates and times. This endpoint
    will try and figure out what is entered but will output incorrect dates
    and times if date format isn't well formatted.

    *Junk in, junk out.*

    """
    if tz not in timezones:
        raise HTTPException(
            status_code=422,
            detail=f"{tz} is not a timzone we have on file",
        )
    if len(arithmetic(date)) <= 1:
        raise HTTPException(
            status_code=404,
            detail=(
                f"{date} cannot be processed. Please enter a date "
                "that can be parsed out by a machine or human."
            ),
        )

    # Function call
    arith = arithmetic(
        date,
        tz,
        years,
        months,
        days,
        hours,
        minutes,
        seconds,
    )

    # Returning Response Model
    return Arithmetic(
        date_entered=date,
        tz=tz,
        years=years,
        months=months,
        days=days,
        hours=hours,
        minutes=minutes,
        returned_date=arith,
    )
