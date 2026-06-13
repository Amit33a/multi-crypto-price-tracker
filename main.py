# Import functions for fetching crypto prices and database operations
from fetch_crypto import fetch_crypto_price
from db import insert_price, get_all_prices


# Fetch the latest cryptocurrency prices from the API
crypto_prices = fetch_crypto_price()


# Store each cryptocurrency price in PostgreSQL
for coin, price in crypto_prices.items():
    insert_price(coin, price)


# Retrieve all stored cryptocurrency prices
rows = get_all_prices()


# Display the retrieved records
print(rows)
   