# -*- coding: utf-8 -*-
from fastapi import APIRouter

# from fastapi.responses import ORJSONResponse
from pendulum import timezones

router = APIRouter(prefix="/timzone")


@router.get("/")
async def timzone():
    """
    Returns list of timezones.
    """
    return {"timezones": list(timezones)}
