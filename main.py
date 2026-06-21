from report import build_report
from fetch_crypto import fetch_crypto_price
from db import create_table, insert_price, get_all_prices


create_table()

crypto_prices = fetch_crypto_price()

if crypto_prices:

    for coin, price in crypto_prices.items():
        insert_price(coin, price)

    rows = get_all_prices()

    report = build_report(rows)

    # PRINT
    print(report)

    # SAVE TO FILE
    with open("reports/crypto_report.txt", "w") as file:
        file.write(report)

else:
    print("Failed to fetch crypto prices.")