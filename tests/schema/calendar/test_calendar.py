# -*- coding: utf-8 -*-
import pytest
import schemathesis
from hypothesis import settings

schemathesis.fixups.install(["fast_api"])
schema = schemathesis.from_uri("http://127.0.0.1:8900/openapi.json")


@pytest.mark.skip(reason="Need to learn Schemathesis.")
@pytest.mark.cal
@schema.parametrize(endpoint="/calendar/arithmetic")
@settings(max_examples=100)
def test_arith(case):
    """
    Schemathesis test for /calendar/arithmetic.
    """
    case.call_and_validate()
