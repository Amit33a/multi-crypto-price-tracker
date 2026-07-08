from unittest.mock import patch

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

from db import get_connection
from db import insert_price


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


from unittest.mock import patch

from db import insert_price


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