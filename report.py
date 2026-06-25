from datetime import datetime

from logger_config import logger


def build_report(rows):

    # Return message if no data exists
    if not rows:
        logger.warning("Report generation skipped: no data available")
        return "No data available."

    logger.info(
        f"Generating report with {len(rows)} database records"
    )

    report = []

    # Add timestamp header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report.append("CRYPTO PRICE REPORT")
    report.append("=" * 30)
    report.append(f"Generated at: {timestamp}")
    report.append("")

    # Format each row
    for row in rows:
        name = row[1].capitalize()
        price = float(row[2])

        report.append(f"{name:<12} ${price:.2f}")

    logger.info("Report generated successfully")

    return "\n".join(report)