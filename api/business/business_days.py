# -*- coding: utf-8 -*-
import re
from typing import Optional

import pendulum as p
from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import ORJSONResponse

from models.business_models import Day
from services.business.working_helpers import (
    delta_working,
    holidays,
    working_days,
)
from services.utilities.base import proper_dates

router = APIRouter(
    prefix="/business",
    default_response_class=ORJSONResponse,
)


@router.get("/days", response_model=Day)
async def business_day(
    date: str = Query(
        default=p.now().to_date_string(),
        description=(
            "Date to count from. Format date as YYYY-MM-DD or MM-DD-YYYY"
        ),
    ),
    days: Optional[int] = Query(
        8,
        description="Number of business days. Default is 8 business days.",
    ),
):
    """
    Calculate working days from given date with given number of days.
    """
    s = re.compile(proper_dates)
    if s.search(date) is None:
        raise HTTPException(
            status_code=400,
            # Might use datefinder here for date correction for examples given.
            detail=(
                f"Date format entered:{date} is incorrect."
                " Date format must be entered as YYYY-MM-DD e.g. 2021-01-01 "
                "or MM-DD-YYYY e.g. 01-01-2021"
            ),
        )
    working_date = working_days(first_date=date, num=days)

    return Day(date=date, days=days, enddate=working_date)


@router.get("/delta")
async def business_delta(
    date_one: str = Query(..., description="First date of dates between."),
    date_two: str = Query(..., description="Second date of dates between."),
):
    """
    Given two dates. This endpoint will output the number of business
    days between them.

    Please enter dates as YYYY-MM-DD as in 2021-01-01 or MM-DD-YYYY as
    in 01-01-2021. Must add the zero for single digit months.

    """
    try:
        s = re.compile(proper_dates)
        if s.search(date_one) is None or s.search(date_two) is None:
            raise HTTPException(
                status_code=400,
                detail=(
                    "Date formatted incorrectly. Must be formatted as "
                    "MM-DD-YYYY(01-01-2020) or YYYY-MM-DDDD(2020-01-01)."
                ),
            )
        delta = delta_working(date_one, date_two)
        return {"business delta": delta}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=error)


@router.get("/holidays/{year}")
async def business_holidays(
    year: int = Path(
        ...,
        description=(
            "Return a list of US holidays for given year."
            " Just enter 4 digit year: 1999."
        ),
    )
):
    """
    This is a list of holidays in the US.
    """
    if year >= 9999:
        raise HTTPException(
            status_code=422,
            detail=(
                "Year cannot be greater than or equal to 9999. Can only go"
                " up to the year 9998. Yeah, there is no 'Party like it's"
                " 9999' in this API 😭"
            ),
        )
    holiday_list = holidays(year=year)
    return {"holidays": holiday_list}
