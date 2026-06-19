from fetch_crypto import fetch_crypto_price
from db import create_table, insert_price, get_all_prices
from report import build_report


create_table()

crypto_prices = fetch_crypto_price()

if crypto_prices:

    for coin, price in crypto_prices.items():
        insert_price(coin, price)

    rows = get_all_prices()

    build_report(rows)

else:
    print("Failed to fetch crypto prices.")