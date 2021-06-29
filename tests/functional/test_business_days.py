# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_working_day_passing():
    # GIVEN /business GET request
    response = client.get(
        "/business/days",
        params={"date": "2021-06-29", "days": 8},
    )

    # THEN assert success response
    assert response.status_code == 200

    # THEN assert return JSON is correct with business date given the number
    # of days
    assert response.json() == {
        "date": "2021-06-29",
        "days": 8,
        "enddate": "2021-07-12",
    }


# Will add parametrized fixtures later
def test_working_day_failing():
    """
    Failing test when incorrect formatted date is entered.
    """

    # GIVEN a GET request to /business with incorrectly formatted date
    response = client.get("/business/days", params={"date": "2-21-2020"})

    # Then status code is 400 for bad request
    assert response.status_code == 400

    # Then detailed message is given for badly formatted date
    assert response.json() == (
        {
            "detail": "Date format entered:2-21-2020 is "
            "incorrect. Date format must be"
            " entered as YYYY-MM-DD e.g. 2021-01-01 or MM-DD-YYYY e.g."
            " 01-01-2021",
        }
    )


# Will create fixtures using both allowed formats.
def test_delta_days_passing():
    """
    Passing test number of business between dates.
    """
    # GIVEN /business/delta GET request
    response = client.get(
        "/business/delta",
        params={"first_date": "2020-06-20", "second_date": "2020-07-21"},
    )

    # THEN status code is 200 for valid date inputs.
    assert response.status_code == 200

    # THEN assert that text is outputted.
    assert response.json() == (
        {
            "first_date": "2020-06-20",
            "second_date": "2020-07-21",
            "business_days": 21,
        }
    )


def test_delta_days_failing():
    """
    Failing test when incorrect formatted date is entered.
    """
    # GIVEN /business/delta GET request
    response = client.get(
        "/business/delta",
        params={"first_date": "1-13-21", "second_date": "2-1-2021"},
    )

    # THEN assert that 400 status is given
    assert response.status_code == 400

    # THEN assert correct detailed error is given
    assert response.json() == (
        {
            "detail": "Date formatted incorrectly. Must be formatted as "
            "MM-DD-YYYY(01-01-2020) or YYYY-MM-DDDD(2020-01-01).",
        }
    )


def test_holidays_list(holidaysdict):
    """
    Passing test for list of holidays for the US.
    """
    # GIVEN /business/holidays/2021
    response = client.get("/business/holidays/2021")

    # THEN assert we receive a 200
    assert response.status_code == 200

    # THEN assert that correct list is outputted
    assert response.json() == {"holidays": holidaysdict}


def test_holidays_list_failing():
    """
    Failing test when 9999 or greater is entered.
    """
    # GIVEN /business/holidays/9999
    response = client.get("/business/holidays/9999")

    # THEN assert we receive 400
    assert response.status_code == 422
    # THEN assert correct detailed exception is given
    assert response.json() == (
        {
            "detail": "Year cannot be greater than or equal to 9999. "
            "Can only go"
            " up to the year 9998. Yeah, there is no 'Party like it's"
            " 9999' in this API 😭",
        }
    )
