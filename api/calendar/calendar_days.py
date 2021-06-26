# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(
    prefix="/calendar",
    default_response_class=ORJSONResponse,
)


@router.get("/")
async def daterange():
    """
    Get date range of given dates.
    """
    ...
