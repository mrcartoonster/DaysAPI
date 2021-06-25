# -*- coding: utf-8 -*-
import re
from typing import Optional

import pendulum as p
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import ORJSONResponse

from services.business.add_working import working_days

router = APIRouter(
    prefix="/business",
    tags=["business"],
    default_response_class=ORJSONResponse,
)

# Clean this up!!!
# Regex for YYYY-MM-DDDD or MM-DDDD-YYYY
proper_dates = (
    r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])|"
    r"^(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])-\d{4}"
)


@router.get("/")
async def business_day(
    date: str = Query(
        default=p.now().to_date_string(),
        description="Date to count from.",
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
            # Might use datefinder here for date correct for examples given.
            detail=(
                f"Date format entered:{date} is incorrect."
                " Date format must be entered as YYYY-MM-DD e.g. 2021-01-01 "
                "or MM-DD-YYYY e.g. 01-01-2021"
            ),
        )
    working_date = working_days(first_date=date, num=days)
    return {"date": working_date}
