# -*- coding: utf-8 -*-
import pytest
import schemathesis
from hypothesis import settings

schemathesis.fixups.install(["fast_api"])
schema = schemathesis.from_uri("http://127.0.0.1:8900/openapi.json")


@pytest.mark.days
@schema.parametrize(endpoint="/business/days")
@settings(max_examples=100)
def test_days(case):
    """
    Schemathesis test for /business/days endpoint.
    """
    case.call_and_validate()
