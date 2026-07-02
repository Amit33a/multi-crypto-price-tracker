from report import build_report
from fetch_crypto import fetch_crypto_price
from db import create_table, insert_price, get_all_prices

from logger_config import logger
from email_sender import send_email


def main():

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
            report = build_report(rows)

            # Step 6: Print report
            print(report)

            # Step 7: Save report to file
            with open("reports/crypto_report.txt", "w") as file:
                file.write(report)

            logger.info("Report saved successfully")

            # Step 8: Send report by email
            if send_email(subject="Daily Crypto Price Report", body=report):
               logger.info("Report email sent successfully")
            else:
                logger.warning("Report email could not be sent")
                
        else:
            logger.warning("Failed to fetch crypto prices")

    except Exception as e:
        logger.error(f"Unexpected error in main application: {e}")

    finally:
        logger.info("Application finished execution")


if __name__ == "__main__":
    main()