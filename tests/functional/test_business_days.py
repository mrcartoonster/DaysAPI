# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_working_day_passing():
    # GIVEN /business GET request
    response = client.get(
        "/business/days",
        params={"date": "2022-02-24", "days": 12},
    )

    # THEN assert success response
    assert response.status_code == 200

    # THEN assert return JSON is correct with business date given the number
    # of days
    assert response.json() == {"date": "Monday, March 14 2022"}


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
        params={"date_one": "12-13-2012", "date_two": "01-18-2013"},
    )

    # THEN status code is 200 for valid date inputs.
    assert response.status_code == 200

    # THEN assert that text is outputted.
    assert response.json() == (
        {
            "business delta": "There are 24 business days between Thursday, "
            "December 13 2012 and Friday, January 18 2013.",
        }
    )


def test_delta_days_failing():
    """
    Failing test when incorrect formatted date is entered.
    """
    # GIVEN /business/delta GET request
    response = client.get(
        "/business/delta",
        params={"date_one": "1-13-21", "date_two": "2-1-2021"},
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
