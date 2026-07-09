from unittest.mock import patch

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

from db import get_connection
from db import insert_price
from db import get_all_prices
import psycopg2


@patch("db.psycopg2.connect")
def test_get_connection(mock_connect):

    connection = get_connection()

    mock_connect.assert_called_once_with(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    assert connection == mock_connect.return_value



@patch("db.psycopg2.connect")
def test_insert_price(mock_connect):

    # Connection object used inside the with block
    mock_connection = mock_connect.return_value.__enter__.return_value

    # Cursor created from that connection
    mock_cursor = mock_connection.cursor.return_value

    # Call the function
    insert_price("bitcoin", 65000)

    # Verify SQL execution
    mock_cursor.execute.assert_called_once_with(
        """
                INSERT INTO multi_crypto_price (crypto_name, price_usd)
                VALUES (%s, %s)
            """,
        ("bitcoin", 65000),
    )

    # Verify cursor cleanup
    mock_cursor.close.assert_called_once()



@patch("db.psycopg2.connect")
def test_get_all_prices(mock_connect):

    # Connection used inside the with block
    mock_connection = mock_connect.return_value.__enter__.return_value

    # Fake cursor
    mock_cursor = mock_connection.cursor.return_value

    # Fake database rows
    expected_rows = [
        (1, "bitcoin", 65000, "2026-07-08"),
        (2, "ethereum", 3200, "2026-07-08"),
    ]

    # fetchall() should return our fake rows
    mock_cursor.fetchall.return_value = expected_rows

    # Call the function
    rows = get_all_prices()

    # Verify SQL query
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM multi_crypto_price ORDER BY created_at DESC"
    )

    # Verify fetchall() was called
    mock_cursor.fetchall.assert_called_once()

    # Verify returned data
    assert rows == expected_rows

    # Verify cursor cleanup
    mock_cursor.close.assert_called_once()


@patch("db.psycopg2.connect")
def test_get_all_prices_connection_failure(mock_connect):

    # Simulate a database connection failure
    mock_connect.side_effect = psycopg2.Error(
        "Unable to connect to database"
    )

    rows = get_all_prices()

    assert rows == []