from datetime import datetime

def build_report(rows):
    # Return message if no data exists
    if not rows:
        return "No data available."

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

    return "\n".join(report)