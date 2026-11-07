
from hypothesis import given, strategies as st
from mobile_data_plan import parse_plan, usage_average, payable_bill


@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    try:
        parse_plan(s)
    except Exception:
        assert False, f"parse_plan crashed with input: {s!r}"


@given(st.text() | st.none())
def test_usage_average_no_crash(s):
    try:
        usage_average(s)
    except Exception:
        assert False, f"usage_average crashed with input: {s!r}"


@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except Exception:
        assert False, f"payable_bill crashed with input: {s!r}"
