# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_arithmetic_passing():
    """
    Test default behaviour for passing.
    """
    # GIVEN GET Request to /calendar/arithmetic
    response = client.get("/arithmetic")

    # THEN assert that 200 is returned.
    assert response.status_code == 200
