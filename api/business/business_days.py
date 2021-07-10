# -*- coding: utf-8 -*-
from typing import Optional

import pendulum as p
from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import ORJSONResponse

from models.business_models import Day, Delta
from services.business.working_helpers import (
    delta_working,
    holidays,
    working_days,
)

router = APIRouter(
    prefix="/business",
    default_response_class=ORJSONResponse,
)


@router.get("/days", response_model=Day)
async def business_day(
    date: str = Query(
        default=p.now().to_date_string(),
        description=(
            "Enter date to add or subtract business days from."
            "You can enter any readable date. Doesn't have to be ISO or RFC"
            " formatted."
        ),
    ),
    days: Optional[int] = Query(
        8,
        description="Number of business days. Default is 8 business days.",
    ),
):
    """
    Calculate working days from given date with given number of days.

    The timezone is set to US/Eastern due to US banks operate only in
    that timezone.

    """
    if working_days(date) is None:
        raise HTTPException(
            status_code=400,
            detail=(
                f"{date} couldn't be parsed as a date. Please enter a human"
                " readable or at least machine readable date."
            ),
        )
    working_date = working_days(date=date, days=days)

    return Day(date=date, days=days, enddate=working_date)


@router.get("/delta", response_model=Delta)
async def business_delta(
    first_date: str = Query(
        default=p.now().to_date_string(),
        description="First date of dates between.",
    ),
    second_date: str = Query(
        default=p.now().add(days=8).to_date_string(),
        description="Second date of dates between.",
    ),
):
    """
    Given two dates. This endpoint will output the number of business
    days between them.

    Dates can be entered in any order. Please enter readable dates.
    Doesn't have to be ISO or RFC formatted dates.

    """
    if delta_working(first_date, second_date) is None:
        raise HTTPException(
            status_code=400,
            detail=(
                "Couldn't parse dates. Please enter human readable or"
                " machine readable dates."
            ),
        )
    delta = delta_working(first_date, second_date)
    return Delta(
        first_date=first_date,
        second_date=second_date,
        business_days=delta,
    )


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
