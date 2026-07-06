from report import build_report


def test_build_report_with_no_data():
    result = build_report([])

    assert result == "No data available."