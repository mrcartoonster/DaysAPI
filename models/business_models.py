# -*- coding: utf-8 -*-
# Location of business api pydantic models
import pendulum as p
from pydantic import BaseModel, Field


class Day(BaseModel):
    """
    JSON Schema for /business/days endpoint.
    """

    date_entered: str = Field(
        default=p.now().to_date_string(),
        description="Date to count business days from.",
    )
    interpreted_date: str = Field(
        default=p.now().to_cookie_string(),
        description=("Interpreted date enterd to make sure it is correct."),
    )
    days: int = Field(
        default=8,
        description="Number of business days to count.",
    )
    enddate: str = Field(
        default=p.now().add(days=8).to_date_string(),
        title="End Date",
        description="Date with business days added.",
    )


class Delta(BaseModel):
    """
    JSON Schema for business/delta endpoint.
    """

    first_date: str = Field(
        default=p.now().to_date_string(),
        description=(
            "First date entered for business days difference calculation."
        ),
    )
    first_interpreted_date = Field(
        default=p.now().to_cookie_string(),
        description="Human readable format of first date entered.",
    )
    second_date: str = Field(
        default=p.now().add(days=8).to_date_string(),
        description="Second date for business days difference calculation.",
    )
    second_interpreted_date = Field(
        default=p.now().add(days=8).to_cookie_string(),
        description="Human readable format of second date entered.",
    )
    business_days: int = Field(
        default=8,
        description="Number of business days after calculation.",
    )
