# Import SMTP library
import smtplib

# Import email configuration
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

# Import application logger
from logger_config import logger


def connect_email_server():
    """
    Connect to the SMTP server and log in.

    Returns:
        SMTP object if successful.
        None if connection fails.
    """

    try:
        logger.info("Connecting to email server")

        # Connect to SMTP server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)

        # Upgrade to encrypted connection
        server.starttls()

        logger.info("TLS encryption enabled")

        # Login to email account
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        logger.info("Logged into email server successfully")

        return server

    except Exception as error:

        logger.error(f"Failed to connect to email server: {error}")

        print(f"Email connection error: {error}")

        return None


def send_email():
    pass
    
