from app.config.settings import REPORT_PATH
from app.database.db import create_table, get_all_prices, insert_price
from app.services.email_sender import send_email
from app.services.fetch_crypto import fetch_crypto_price
from app.services.report import build_report
from app.utils.logger import logger


def create_application():
    def application():
        logger.info("Application started")

        try:
            # Step 1: Create table
            create_table()

            # Step 2: Fetch crypto prices
            crypto_prices = fetch_crypto_price()

            if crypto_prices:
                logger.info("Saving crypto prices to database")

                # Step 3: Insert into DB
                for coin, price in crypto_prices.items():
                    insert_price(coin, price)

                # Step 4: Fetch from DB
                rows = get_all_prices()

                logger.info("Generating report")

                # Step 5: Generate report
                report = build_report(rows, logger)

                # Step 6: Print report
                print(report)

                # Step 7: Save report to file
                with open(REPORT_PATH, "w", encoding="utf-8") as file:
                    file.write(report)

                logger.info("Report saved successfully")

                # Step 8: Send report by email
                if send_email(
                    subject="Daily Crypto Price Report",
                    body="Please find today's cryptocurrency report attached.",
                    attachment_path=REPORT_PATH,
                ):
                    logger.info("Report email sent successfully")
                else:
                    logger.warning("Report email could not be sent")

            else:
                logger.warning("Failed to fetch crypto prices")

        except Exception as e:
            logger.error(f"Unexpected error in main application: {e}")

        finally:
            logger.info("Application finished execution")

    return application
