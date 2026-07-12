# Import os module to access environment variables
import os

# Import load_dotenv to read variables from the .env file
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


# Get a required environment variable
def get_required_env(name):
    """
    Return the value of a required environment variable.

    Raises:
        RuntimeError: If the environment variable is missing.
    """

    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")

    return value


# Get a required integer environment variable
def get_required_int(name):
    """
    Return a required integer environment variable.

    Raises:
        RuntimeError: If the variable is missing.
        ValueError: If the value is not a valid integer.
    """

    value = get_required_env(name)

    try:
        return int(value)

    except ValueError:
        raise ValueError(
            f"Invalid integer value for environment variable '{name}': {value}"
        )


# Database Configuration
DB_HOST = get_required_env("DB_HOST")
DB_PORT = get_required_int("DB_PORT")
DB_NAME = get_required_env("DB_NAME")
DB_USER = get_required_env("DB_USER")
DB_PASSWORD = get_required_env("DB_PASSWORD")


# API Configuration
REQUEST_TIMEOUT = get_required_int("REQUEST_TIMEOUT")
MAX_RETRIES = get_required_int("MAX_RETRIES")


# Email Configuration
EMAIL_HOST = get_required_env("EMAIL_HOST")
EMAIL_PORT = get_required_int("EMAIL_PORT")
EMAIL_USER = get_required_env("EMAIL_USER")
EMAIL_PASSWORD = get_required_env("EMAIL_PASSWORD")
EMAIL_RECEIVER = get_required_env("EMAIL_RECEIVER")


# Report configuration
REPORT_DIRECTORY = "reports"
REPORT_FILE = "crypto_report.txt"
REPORT_PATH = f"{REPORT_DIRECTORY}/{REPORT_FILE}"
