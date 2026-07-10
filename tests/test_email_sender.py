from unittest.mock import patch

from email_sender import send_email


@patch("email_sender.connect_email_server")
def test_send_email_success(mock_connect):

    # Fake SMTP server
    mock_server = mock_connect.return_value

    # Call the function
    result = send_email(
        subject="Test Subject",
        body="Test Body"
    )

    # Verify email was sent
    mock_server.send_message.assert_called_once()

    # Verify SMTP connection was closed
    mock_server.quit.assert_called_once()

    # Verify function returned success
    assert result is True