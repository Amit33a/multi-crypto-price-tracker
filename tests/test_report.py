from datetime import datetime

from report import build_report


def test_build_report_with_no_data():
    result = build_report([])

    assert result == "No data available."


def test_build_report_with_valid_data():

    rows = [(1, "bitcoin", 65000, datetime(2026, 7, 6, 10, 30, 0))]

    result = build_report(rows)

    assert "Bitcoin" in result
    assert "$65000.00" in result
    assert "CRYPTO PRICE REPORT" in result


def test_build_report_with_multiple_cryptocurrencies():

    rows = [
        (1, "bitcoin", 65000, datetime(2026, 7, 6, 10, 30, 0)),
        (2, "ethereum", 3200, datetime(2026, 7, 6, 10, 30, 0)),
        (3, "solana", 180, datetime(2026, 7, 6, 10, 30, 0)),
        (4, "binancecoin", 720, datetime(2026, 7, 6, 10, 30, 0)),
    ]

    report = build_report(rows)

    assert "Bitcoin" in report
    assert "Ethereum" in report
    assert "Solana" in report
    assert "Binancecoin" in report

    assert "$65000.00" in report
    assert "$3200.00" in report
    assert "$180.00" in report
    assert "$720.00" in report
