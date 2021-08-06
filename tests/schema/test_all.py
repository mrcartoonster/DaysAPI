import pytest
import schemathesis
from hypothesis import settings


schemathesis.fixups.install(["fast_api"])
schema = schemathesis.from_uri("http://127.0.0.1:8900/openapi.json")


@pytest.mark.all
@schema.parametrize()
@settings(max_examples=30)
def test_api(case):
    case.call_and_validate()


@pytest.mark.days
@schema.parametrize(endpoint="/business/days")
def test_days(case):
    """
    Schemathesis test for /business/days endpoint.
    """
    case.call_and_validate()


@pytest.mark.cal
@schema.parametrize(endpoint="/calendar/arithmetic")
def test_arith(case):
    """
    Schemathesis test for /calendar/arithmetic.
    """
    case.call_and_validate()
