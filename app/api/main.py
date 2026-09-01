from app.api.dependencies import get_dependencies
from app.services.crypto_workflow import run_crypto_workflow


def create_application():
    dependencies = get_dependencies()

    def application():
        logger = dependencies["logger"]

        logger.info("Application started")

        try:
            success = run_crypto_workflow(
                logger,
                dependencies["create_table"],
                dependencies["fetch_crypto_price"],
                dependencies["insert_price"],
                dependencies["get_all_prices"],
                dependencies["build_report"],
                dependencies["send_email"],
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
