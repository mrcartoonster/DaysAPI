# -*- coding: utf-8 -*-
# Location of business api pydantic models
import pendulum as p
from pydantic import BaseModel


class Day(BaseModel):
    """
    JSON Schema for /business/days endpoint.
    """

    date: str = p.now().to_date_string()
    days: int = 8
    enddate: str = p.now().add(days=8).to_date_string()


class Delta(BaseModel):
    """
    JSON Schema for business/delta endpoint.
    """

    first_date: str = p.now().to_date_string()
    second_date: str = p.now().add(days=8).to_date_string()
    business_days: int = 8
