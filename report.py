def build_report(rows):
    # Return message if no data exists
    if not rows:
        return "No data available."

    report = []

    # Report header
    report.append("\nCrypto Price Report")
    report.append("=" * 30)

    # Format each database row
    for row in rows:
        name = row[1].capitalize()
        price = float(row[2])

        report.append(f"{name:<12} ${price:.2f}")

    # Convert list to final string output
    return "\n".join(report)