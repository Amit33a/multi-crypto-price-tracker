from unittest.mock import MagicMock, patch

from app.services.crypto_workflow import run_crypto_workflow


def test_run_crypto_workflow_success():
    logger = MagicMock()

    crypto_prices = {
        "bitcoin": 65000,
        "ethereum": 3200,
    }

    rows = [
        (1, "bitcoin", 65000, "2026-08-23 10:30:00"),
        (2, "ethereum", 3200, "2026-08-23 10:30:00"),
    ]

    with (
        patch("app.services.crypto_workflow.create_table") as mock_create_table,
        patch(
            "app.services.crypto_workflow.fetch_crypto_price",
            return_value=crypto_prices,
        ) as mock_fetch,
        patch("app.services.crypto_workflow.insert_price") as mock_insert,
        patch(
            "app.services.crypto_workflow.get_all_prices",
            return_value=rows,
        ) as mock_get_all_prices,
        patch(
            "app.services.crypto_workflow.build_report",
            return_value="Crypto Report",
        ) as mock_build_report,
        patch(
            "app.services.crypto_workflow.send_email",
            return_value=True,
        ) as mock_send_email,
        patch("builtins.open") as mock_open,
        patch("builtins.print") as mock_print,
    ):
        run_crypto_workflow(logger)

    mock_create_table.assert_called_once()

    mock_fetch.assert_called_once()

    assert mock_insert.call_count == 2

    mock_insert.assert_any_call("bitcoin", 65000)
    mock_insert.assert_any_call("ethereum", 3200)

    mock_get_all_prices.assert_called_once()

    mock_build_report.assert_called_once_with(rows, logger)

    mock_print.assert_called_once_with("Crypto Report")

    mock_open.assert_called_once()

    mock_send_email.assert_called_once()


def test_run_crypto_workflow_when_no_prices():
    logger = MagicMock()

    with (
        patch("app.services.crypto_workflow.create_table") as mock_create_table,
        patch(
            "app.services.crypto_workflow.fetch_crypto_price",
            return_value={},
        ) as mock_fetch,
        patch("app.services.crypto_workflow.insert_price") as mock_insert,
        patch("app.services.crypto_workflow.get_all_prices") as mock_get_all_prices,
        patch("app.services.crypto_workflow.build_report") as mock_build_report,
        patch("app.services.crypto_workflow.send_email") as mock_send_email,
    ):
        run_crypto_workflow(logger)

    mock_create_table.assert_called_once()

    mock_fetch.assert_called_once()

    logger.warning.assert_called_once_with("Failed to fetch crypto prices")

    mock_insert.assert_not_called()
    mock_get_all_prices.assert_not_called()
    mock_build_report.assert_not_called()
    mock_send_email.assert_not_called()
