# -*- coding: utf-8 -*-
import pendulum as p
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse
from pendulum import timezones

from models.calendar_models import Arithmetic, Diff
from services.calendar.calendar_helpers import arithmetic, differ, isoformatter

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
            detail=f"{tz} is not a timezone we have on file.",
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


@router.get("/difference", response_model=Diff)
async def difference(
    date_one: str = Query(
        default=p.now().to_date_string(),
        title="first date",
        description="First date to get difference",
    ),
    date_two: str = Query(
        default=p.now().add(months=2).to_date_string(),
        title="second date",
        description="Second date to get calendar difference",
    ),
    tz: str = Query(
        default="UTC",
        title="Time Zone",
        description="Please entered prefered timzone. Use `IANA` format.",
    ),
):
    """
    This endpoint takes in two dates and calculates the difference for
    you with the queries you enter.
    """
    if tz not in timezones:
        raise HTTPException(
            status_code=400,
            detail=f"{tz} is not a timzone we have on file.",
        )
    if difference(date_one=date_one, date_two=date_two, tz=tz) == []:
        raise HTTPException(
            status_code=400,
            detail=(
                "Couldn't parse dates entered. Please enter human or machine"
                " readable dates."
            ),
        )

    # Function call
    diff = differ(date_one, date_two, tz)
    date_1 = isoformatter(date_one)
    date_2 = isoformatter(date_two)

    # Response Model
    return Diff(
        period_one={
            "date_one": date_one,
            "formatted_date_one": date_1,
        },
        period_two={
            "date_two": date_two,
            "formatted_date_two": date_2,
        },
        difference=diff,
    )
