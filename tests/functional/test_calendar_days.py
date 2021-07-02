# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_arithmetic_passing():
    """
    Test default behaviour for passing.
    """
    # GIVEN GET Request to /calendar/arithmetic
    response = client.get(
        "/calendar/arithmetic",
        params={"date": "1-1-2021", "days": 5},
    )

    # THEN assert that 200 is returned.
    assert response.status_code == 200

    # THEN assert that respon
    assert response.json() == {
        "date_entered": "1-1-2021",
        "tz": "UTC",
        "years": 0,
        "months": 0,
        "days": 5,
        "hours": 0,
        "minutes": 0,
        "seconds": 0,
        "returned_date": "2021-01-06 00:00:00",
    }


def test_arithmetic_badly_formatted_date_failing():
    """
    Ensure failure when badly formatted date is entered.
    """
    # GIVEN a GET request with poorly formatted date
    response = client.get(
        "/calendar/arithmetic",
        params={"date": "2 j 2011", "minutes": 22},
    )

    # THEN assert that 422 is returned
    assert response.status_code == 404

    # THEN assert that error message is returned
    assert response.json() == {
        "detail": (
            "2 j 2011 cannot be processed. Please enter a date "
            "that can be parsed out by a machine or human."
        ),
    }


def test_arithmetic_incorrect_tz_failing():
    """
    Ensure that when incorrect timezone is entered that error message is
    given.
    """
    # GIVEN a GET request with incorrect timzone
    ...
