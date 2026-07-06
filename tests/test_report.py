from datetime import datetime
from report import build_report


def test_build_report_with_no_data():
    result = build_report([])

    assert result == "No data available."

def test_build_report_with_valid_data():

    rows = [
        (
            1,
            "bitcoin",
            65000,
            datetime(2026, 7, 6, 10, 30, 0)
        )
    ]

    result = build_report(rows)

    assert "Bitcoin" in result
    assert "$65000.00" in result
    assert "CRYPTO PRICE REPORT" in result