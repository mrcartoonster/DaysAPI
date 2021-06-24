# -*- coding: utf-8 -*-
from typing import Optional

import pendulum as p
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel, Field

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


class WorkingDays(BaseModel):
    date: Optional[str] = Field(
        p.now().to_date_string(),
        regex=proper_dates,
        description="Date to count from for business days.",
    )
    number: int = Field(
        default=8,
        description="Number of business days to add",
    )


@router.post("/")
async def business_day(date: WorkingDays):
    """
    Calculate working days from given date with given number of days.
    """
    days = working_days(first_date=date.date, num=date.number)
    return {"date": days}
