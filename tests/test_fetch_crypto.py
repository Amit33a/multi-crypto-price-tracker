from unittest.mock import patch
import requests

from fetch_crypto import fetch_crypto_price


@patch("fetch_crypto.requests.get")
def test_fetch_crypto_price_success(mock_get):

    mock_response = mock_get.return_value

    mock_response.raise_for_status.return_value = None

    mock_response.json.return_value = {
        "bitcoin": {"usd": 65000},
        "ethereum": {"usd": 3200},
        "solana": {"usd": 180},
        "binancecoin": {"usd": 720},
    }

    result = fetch_crypto_price()

    assert result == {
        "bitcoin": 65000,
        "ethereum": 3200,
        "solana": 180,
        "binancecoin": 720,
    }


@patch("fetch_crypto.requests.get")
def test_fetch_crypto_price_request_failure(mock_get):

    mock_get.side_effect = requests.exceptions.ConnectionError(
        "Unable to connect"
    )

    result = fetch_crypto_price()

    assert result is None


@patch("fetch_crypto.requests.get")
def test_fetch_crypto_price_with_missing_data(mock_get):

    mock_response = mock_get.return_value

    mock_response.raise_for_status.return_value = None

    mock_response.json.return_value = {
        "bitcoin": {"usd": 65000},
        "ethereum": {"usd": 3200},
        "solana": {},
        "binancecoin": {"usd": 720},
    }

    result = fetch_crypto_price()

    assert result is None