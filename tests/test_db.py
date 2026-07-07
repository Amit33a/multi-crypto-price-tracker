from unittest.mock import patch

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

from db import get_connection


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