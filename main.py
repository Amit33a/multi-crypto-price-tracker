from fetch_crypto import fetch_crypto_price
from db import create_table, insert_price, get_all_prices


create_table()

crypto_prices = fetch_crypto_price()

for coin, price in crypto_prices.items():
    insert_price(coin, price)

rows = get_all_prices()

print(rows)