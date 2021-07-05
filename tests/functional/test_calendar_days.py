# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

success_response = {
    "period_one": {"date_one": "07-06-2022"},
    "period_two": {"date_two": "11-08-2022"},
    "difference": {
        "time_zone": "UTC",
        "years": 0,
        "months": 4,
        "weeks": 17,
        "days": 125,
        "hours": 3000,
        "minutes": 180000,
        "seconds": 10800000,
        "words": "4 months 2 days",
    },
}


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
    response = client.get(
        "/calendar/arithmetic",
        params={"date": "02-02-2021", "tz": "US/Conti"},
    )

    # THEN assert response is 422
    assert response.status_code == 422

    # THEN assert correct error message is given
    assert response.json() == (
        {"detail": "US/Conti is not a timezone we have on file."}
    )


def test_difference_passing():
    """
    Create test for correct dates entered passing.
    """
    # GIVEN a GET request with valid date.
    response = client.get(
        "/calendar/difference",
        params={"date_one": "07-06-2022", "date_two": "11-08-2022"},
    )

    # THEN assert success 200
    assert response.status_code == 200

    # THEN assert response matches
    assert response.json() == success_response


def test_difference_failing_formatted_date():
    """
    Create failing test when poorly formatted test is entered.
    """
    ...
