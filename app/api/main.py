from app.services.crypto_workflow import run_crypto_workflow
from app.utils.logger import logger


def create_application():
    def application():
        logger.info("Application started")

        try:
            run_crypto_workflow(logger)

        except Exception as e:
            logger.error(f"Unexpected error in main application: {e}")

        finally:
            logger.info("Application finished execution")

    return application
