# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_working_day_passing():
    # GIVEN /business GET request
    response = client.get(
        "/business",
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
    response = client.get("/business", params={"date": "2-21-2020"})

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
