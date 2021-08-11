# -*- coding: utf-8 -*-
import pytest
import schemathesis
from hypothesis import settings

schemathesis.fixups.install(["fast_api"])
schema = schemathesis.from_uri("http://127.0.0.1:8900/openapi.json")


@pytest.mark.skip(reason="Need to learn Schemathesis.")
@pytest.mark.all
@schema.parametrize()
@settings(max_examples=30)
def test_api(case):
    case.call_and_validate()
