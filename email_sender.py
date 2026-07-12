# Import SMTP library
import smtplib

# Import operating system utilities
import os

# Import email configuration
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD, EMAIL_RECEIVER

# Import application logger
from logger_config import logger

# Import EmailMessage to create and format email messages
from email.message import EmailMessage


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


# Create and send a plain text email
def send_email(subject, body, attachment_path=None) -> bool:
    """
    Send a plain text email.
    """

    # Connect to the email server
    server = connect_email_server()

    # Stop if the connection could not be established
    if not server:
        return False

    try:

        logger.info("Creating email message")

        # Create a new email message
        message = EmailMessage()

        # Set email details
        message["Subject"] = subject
        message["From"] = EMAIL_USER
        message["To"] = EMAIL_RECEIVER

        # Add email body
        message.set_content(body)

        # Attach report file if provided
        if attachment_path:

            logger.info(f"Attaching file: {attachment_path}")

            with open(attachment_path, "rb") as file:

                message.add_attachment(
                    file.read(),
                    maintype="text",
                    subtype="plain",
                    filename=os.path.basename(attachment_path),
                )

        logger.info("Sending email")

        # Send the email
        server.send_message(message)

        logger.info("Email sent successfully")

        return True

    except Exception as error:

        logger.error(f"Failed to send email: {error}")

        print(f"Email error: {error}")

        return False

    finally:

        # Close the connection to the email server
        server.quit()

        logger.info("Disconnected from email server")
