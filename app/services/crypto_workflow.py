from app.config.settings import REPORT_PATH


def run_crypto_workflow(
    logger,
    create_table,
    fetch_crypto_price,
    insert_price,
    get_all_prices,
    build_report,
    send_email,
):
    # Step 1: Create database table
    create_table()

    # Step 2: Fetch cryptocurrency prices
    crypto_prices = fetch_crypto_price()

    if not crypto_prices:
        logger.warning("Failed to fetch crypto prices")
        return False

    logger.info("Saving crypto prices to database")

    # Step 3: Insert prices into database
    for coin, price in crypto_prices.items():
        insert_price(coin, price)

    # Step 4: Retrieve prices from database
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
        return False

    return True
