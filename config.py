# Import os module to access environment variables
import os

# Import load_dotenv to read variables from the .env file
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# Database configuration values
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))