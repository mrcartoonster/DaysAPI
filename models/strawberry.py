# -*- coding: utf-8 -*-
import pendulum as p
import strawberry
from pydantic import BaseModel, Field


class PeriodOne(BaseModel):
    """
    JSON Schema Response model for first entered date.
    """

    date_one: str = Field(
        default=p.now().to_datetime_string(),
        title="Date One",
        description="First date entered",
    )
    formatted_date_one: str = Field(
        default=p.now().to_iso8601_string(),
        title="Date One formatted",
        description="Formatted for Humans.",
    )


@strawberry.experimental.pydantic.error_type(
    model=PeriodOne,
    fields=[
        "date_one",
        "formatted_date_one",
    ],
)
class PeriodOneError:
    pass
