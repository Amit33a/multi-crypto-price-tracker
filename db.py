# Import PostgreSQL adapter to connect Python with PostgreSQL database
import psycopg2

# Import database configuration values
from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


# Create and return a PostgreSQL database connection
def get_connection():

    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


# Create the table if it does not already exist
def create_table():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS multi_crypto_price (
            id SERIAL PRIMARY KEY,
            crypto_name VARCHAR(50) NOT NULL,
            price_usd NUMERIC(18,8) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()

    cur.close()
    conn.close()


# Insert a cryptocurrency price into the database
def insert_price(crypto_name, price):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO multi_crypto_price (crypto_name, price_usd)
        VALUES (%s, %s)
    """, (crypto_name, price))

    conn.commit()

    cur.close()
    conn.close()


# Retrieve all cryptocurrency prices from the database
def get_all_prices():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM multi_crypto_price ORDER BY created_at DESC"
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows