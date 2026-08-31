from unittest.mock import MagicMock, patch

from app.services.crypto_workflow import run_crypto_workflow


def test_run_crypto_workflow_success():
    logger = MagicMock()

    create_table = MagicMock()

    fetch_crypto_price = MagicMock(
        return_value={
            "bitcoin": 65000,
            "ethereum": 3200,
        }
    )

    insert_price = MagicMock()

    get_all_prices = MagicMock(
        return_value=[
            (1, "bitcoin", 65000, "2026-08-23 10:30:00"),
            (2, "ethereum", 3200, "2026-08-23 10:30:00"),
        ]
    )

    build_report = MagicMock(return_value="Crypto Report")

    send_email = MagicMock(return_value=True)

    with (
        patch("builtins.open") as mock_open,
        patch("builtins.print") as mock_print,
    ):
        result = run_crypto_workflow(
            logger,
            create_table,
            fetch_crypto_price,
            insert_price,
            get_all_prices,
            build_report,
            send_email,
        )

    assert result is True

    create_table.assert_called_once()
    fetch_crypto_price.assert_called_once()

    assert insert_price.call_count == 2

    get_all_prices.assert_called_once()
    build_report.assert_called_once()
    send_email.assert_called_once()

    mock_open.assert_called_once()
    mock_print.assert_called_once_with("Crypto Report")


def test_run_crypto_workflow_when_no_prices():
    logger = MagicMock()

    create_table = MagicMock()
    fetch_crypto_price = MagicMock(return_value={})

    insert_price = MagicMock()
    get_all_prices = MagicMock()
    build_report = MagicMock()
    send_email = MagicMock()

    result = run_crypto_workflow(
        logger,
        create_table,
        fetch_crypto_price,
        insert_price,
        get_all_prices,
        build_report,
        send_email,
    )

    assert result is False

    create_table.assert_called_once()
    fetch_crypto_price.assert_called_once()

    insert_price.assert_not_called()
    get_all_prices.assert_not_called()
    build_report.assert_not_called()
    send_email.assert_not_called()

    logger.warning.assert_called_once_with("Failed to fetch crypto prices")
