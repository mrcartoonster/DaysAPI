# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_days_ago_passing():
    # GIVEN GET request to calendar/daysago
    response = client.get(
        "/calendar/daysago",
        params={"date": "2020-06-29", "days": 8},
    )

    # THEN assert the 200 response
    assert response.status_code == 200

    # THEN assert correct date is given
    assert response.json() == {
        "date": "2020-06-29",
        "days": 8,
        "past_date": "2020-06-21",
    }


def test_days_ago_failing():
    """
    Failing test when incorrect date format entered.
    """

    # GIVEN GET reqeust to calendar/daysago
    response = client.get(
        "calendar/daysago",
        params={"date": "1-06-2020", "days": 8},
    )

    # THEN assert the 400 is returned.
    assert response.status_code == 400

    # THEN assert correct exception is given
    assert response.json() == {
        "detail": "Date format: 1-06-2020 is incorrect.",
    }
