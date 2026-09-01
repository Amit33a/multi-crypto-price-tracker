from app.database.db import create_table, get_all_prices, insert_price
from app.services.email_sender import send_email
from app.services.fetch_crypto import fetch_crypto_price
from app.services.report import build_report
from app.utils.logger import logger


def get_dependencies():
    return {
        "logger": logger,
        "create_table": create_table,
        "fetch_crypto_price": fetch_crypto_price,
        "insert_price": insert_price,
        "get_all_prices": get_all_prices,
        "build_report": build_report,
        "send_email": send_email,
    }
