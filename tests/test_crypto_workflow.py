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
        patch("app.services.crypto_workflow.create_table"),
        patch(
            "app.services.crypto_workflow.fetch_crypto_price",
            return_value=crypto_prices,
        ),
        patch("app.services.crypto_workflow.insert_price"),
        patch(
            "app.services.crypto_workflow.get_all_prices",
            return_value=rows,
        ),
        patch(
            "app.services.crypto_workflow.build_report",
            return_value="Crypto Report",
        ),
        patch(
            "app.services.crypto_workflow.send_email",
            return_value=True,
        ),
        patch("builtins.open"),
        patch("builtins.print"),
    ):
        result = run_crypto_workflow(logger)

    assert result is True


def test_run_crypto_workflow_when_no_prices():
    logger = MagicMock()

    with (
        patch("app.services.crypto_workflow.create_table"),
        patch(
            "app.services.crypto_workflow.fetch_crypto_price",
            return_value={},
        ),
    ):
        result = run_crypto_workflow(logger)

    assert result is False

    logger.warning.assert_called_once_with("Failed to fetch crypto prices")
