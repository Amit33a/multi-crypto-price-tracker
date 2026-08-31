from app.database.db import create_table, get_all_prices, insert_price
from app.services.crypto_workflow import run_crypto_workflow
from app.services.email_sender import send_email
from app.services.fetch_crypto import fetch_crypto_price
from app.services.report import build_report
from app.utils.logger import logger


def create_application():
    def application():
        logger.info("Application started")

        try:
            success = run_crypto_workflow(
                logger,
                create_table,
                fetch_crypto_price,
                insert_price,
                get_all_prices,
                build_report,
                send_email,
            )

            if success:
                logger.info("Crypto workflow completed successfully")
            else:
                logger.warning("Crypto workflow failed")

        except Exception as e:
            logger.error(f"Unexpected error in main application: {e}")

        finally:
            logger.info("Application finished execution")

    return application
