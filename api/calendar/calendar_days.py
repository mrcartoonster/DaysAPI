# -*- coding: utf-8 -*-
import pendulum as p
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse
from pendulum import timezones

from models.calendar_models import Arithmetic  # , Difference
from services.calendar.calendar_helpers import arithmetic

router = APIRouter(
    prefix="/calendar",
    default_response_class=ORJSONResponse,
)


# May use Depends on this. There's a lot of queries and a lot of lines
# of code.
@router.get("/arithmetic", response_model=Arithmetic)
async def calendar_arithmetic(
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
    This endpoint will take in a date number of years, months, days,
    hours, minutes, and seconds as query parameters and return the date
    with the addtion or subtraction produced from entered query
    parameters.

    This endpoint can do addition and subtraction. To do subtraction just add
    `-` befor the integer like so `-8` and the endpoint will subtract based
    on the query.

    **Note**: Please enter properly formatted dates and optionally times.
    This endpoint will try and figure out what is entered but will output
    incorrect dates and times if date format isn't well formatted.

    """
    if tz not in timezones:
        raise HTTPException(
            status_code=422,
            detail=f"{tz} is not a timzone we have on file",
        )
    if arithmetic(date) == []:
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


@router.get("/difference")
async def difference():
    """
    This endpoint takes in two dates and calculates the difference for
    you with the queries you enter.
    """
    ...
