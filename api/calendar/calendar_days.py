# -*- coding: utf-8 -*-
import pendulum as p
from fastapi import APIRouter, HTTPException, Query

# from fastapi.responses import ORJSONResponse
from pendulum import timezones

from models.calendar_models import (
    Arithmetic,
    Diff,
    FormatRequest,
    FormatResponse,
    WeekDay,
    WeekEnd,
)
from services.business.working_helpers import to_day_string
from services.calendar.calendar_helpers import (
    arithmetic,
    atom_string,
    cookie_string,
    day_of_week,
    differ,
    iso_8601,
    isoformatter,
    rfc_822,
    rfc_850,
    rfc_1036,
    rfc_1123,
    rfc_2822,
    rfc_3339,
    rss,
    w3c,
    weekday,
    weekend,
)

router = APIRouter(
    prefix="/calendar",
    # default_response_class=ORJSONResponse,
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
    if arithmetic(date) is None:
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
        interpreted_date=to_day_string(date),
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
    tz_1: str = Query(
        default="UTC",
        title="First date time zone",
        description="Please entered prefered timzone. Use `IANA` format.",
    ),
    date_two: str = Query(
        default=p.now().add(months=2).to_date_string(),
        title="second date",
        description="Second date to get calendar difference",
    ),
    tz_2: str = Query(
        default="UTC",
        title="Time Zone",
        description="Please entered prefered timzone. Use `IANA` format.",
    ),
):
    """
    This endpoint takes in two dates and calculates the difference for
    you with the queries you enter.
    """
    if tz_1 not in timezones or tz_2 not in timezones:
        raise HTTPException(
            status_code=400,
            detail="Cannot locate timezone.",
        )
    if (
        difference(date_one=date_one, tz_1=tz_1, date_two=date_two, tz_2=tz_2)
        is None
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Couldn't parse dates entered. Please enter human or machine"
                " readable dates."
            ),
        )

    # Function call
    diff = differ(date_one, date_two, tz_1, tz_2)
    date_1 = isoformatter(date_one, tz_1)
    date_2 = isoformatter(date_two, tz_2)

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


@router.get("/is_weekday", response_model=WeekDay)
async def is_weekday(
    date: str = Query(
        default=p.now().to_date_string(),
        description="Date to check for weekday.",
    ),
):
    """
    Endpoint will return True or False of date entered is a weekday.

    If date is a Saturday or Sunday, then `false` will be returned.

    """
    if weekday(date) is None:
        raise HTTPException(
            status_code=422,
            detail=f"{date} isn't a date that can be interepreted.",
        )
    wk = weekday(date)
    iso = isoformatter(date)
    dw = day_of_week(date)

    return WeekDay(
        date_entered=date,
        isoformat=iso,
        is_weekday=wk,
        day_of_week=dw,
    )


@router.get("/is_weekend", response_model=WeekEnd)
async def is_weekend(
    date: str = Query(
        default=p.now().to_date_string(),
        description="Checks if date given is a weekend.",
    )
):
    """
    Endpoint will return True if date falls on the weekend, Saturday or
    Sunday.
    """
    if weekend(date) is None:
        raise HTTPException(
            status_code=422,
            detail=f"{date} isn't a date that can be interepreted.",
        )
    wk = weekend(date)
    iso = isoformatter(date)
    dw = day_of_week(date)

    return WeekEnd(
        date_entered=date,
        isoformat=iso,
        is_weekend=wk,
        day_of_week=dw,
    )


@router.post("/date_format", response_model=FormatResponse)
async def date_format(date_format: FormatRequest):
    """
    Enter dates with the the format you'd want them returned in.

    You can enter text that contains the date(s) and this endpoint
    will try to parse out the date(s) and return a list of just the
    date(s) in requested format chosen. Results may very.
    May give extra dates or less dates.

    The formats are:

    * **Cookie String**:
        * `'Thursday, 25-Dec-1975 14:15:16 EST'`
    * **Atom Strin**g:
        * `'1975-12-25T14:15:16-05:00'`
    * **ISO-8601**(default):
        * `'1975-12-25T14:15:16-0500'`
    * **RFC-822**:
        * `'Thu, 25 Dec 75 14:15:16 -0500'`
    * **RFC-850**:
        * `'Thursday, 25-Dec-75 14:15:16 EST'`
    * **RFC-1036**:
        * `'Thu, 25 Dec 75 14:15:16 -0500'`
    * **RFC-1123**:
        * `'Thu, 25 Dec 1975 14:15:16 -0500'`
    * **RFC-2822**:
        * `'Thu, 25 Dec 1975 14:15:16 -0500'`
    * **RFC-3339**:
        * `'1975-12-25T14:15:16-05:00'`
    * **RSS**:
        * `'Thu, 25 Dec 1975 14:15:16 -0500'`
    * **W3C**:
        * `'1975-12-25T14:15:16-05:00'`

    """
    if date_format.time_zone not in timezones:
        raise HTTPException(
            status_code=422,
            detail=(
                f"'{date_format.time_zone}' "
                "is not a time zone we have on file.",
            ),
        )

    if date_format.dateform.value == "atom_string":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=atom_string(
                date_format.dates,
                date_format.time_zone,
            ),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "cookie_string":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=cookie_string(
                date_format.dates,
                date_format.time_zone,
            ),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "iso_8601":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=iso_8601(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "rfc_822":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=rfc_822(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "rfc_850":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=rfc_850(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "rfc_1036":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=rfc_1036(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "rfc_1123":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=rfc_1123(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "rfc_2822":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=rfc_2822(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "rfc_3339":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=rfc_3339(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "rss":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=rss(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )

    if date_format.dateform.value == "w3c":
        return FormatResponse(
            entered_dates=date_format.dates,
            format_selection=date_format.dateform,
            formatted_list=w3c(date_format.dates, date_format.time_zone),
            time_zone=date_format.time_zone,
        )
