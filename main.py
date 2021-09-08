# -*- coding: utf-8 -*-
from fastapi import FastAPI

from api.business import business_days
from api.calendar import calendar_days

# from api.timezones import timezone


def create_application() -> FastAPI:
    """
    FastAPI application instance.
    """
    application = FastAPI(
        title="Business Days for All!",
        description="Simple API that computes business days and dates.",
        version="0.0.1",
        docs_url="/",
    )

    # routers
    application.include_router(business_days.router, tags=["Business"])
    application.include_router(calendar_days.router, tags=["Calendar"])
    # application.include_router(timezone.router, tags=["Time Zone"])

    return application


app = create_application()
