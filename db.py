# Import PostgreSQL adapter to connect Python with PostgreSQL database
import psycopg2

# Import os module to access environment variables
import os

# Import load_dotenv to read variables from the .env file
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# Create and return a PostgreSQL database connection
def create_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )


# Create the table if it does not already exist
def create_table():

    conn = create_connection()
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

    conn = create_connection()
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

    conn = create_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM multi_crypto_price ORDER BY created_at DESC"
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows