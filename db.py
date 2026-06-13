# Import PostgreSQL adapter to connect Python with PostgreSQL database
import psycopg2

# Import os module to access environment variables
import os

# Import load_dotenv to read variables from the .env file
from dotenv import load_dotenv


# Load environment variables from the .env file into the application
load_dotenv()


# Insert a cryptocurrency price into the database
def insert_price(crypto_name, price):

    # Establish connection with PostgreSQL using credentials from .env
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the table if it does not already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS multi_crypto_price (
            id SERIAL PRIMARY KEY,
            crypto_name VARCHAR(50) NOT NULL,
            price_usd NUMERIC(18,8) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert the cryptocurrency name and price into the table
    cursor.execute("""
        INSERT INTO multi_crypto_price (crypto_name, price_usd)
        VALUES (%s, %s)
    """, (crypto_name, price))

    # Save the changes made to the database
    conn.commit()

    # Close the cursor to free database resources
    cursor.close()

    # Close the database connection
    conn.close()


# Retrieve all cryptocurrency prices from the database
def get_all_prices():

    # Establish connection with PostgreSQL using credentials from .env
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Retrieve all records ordered by latest inserted time
    cursor.execute(
        "SELECT * FROM multi_crypto_price ORDER BY created_at DESC"
    )

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Close the cursor to free database resources
    cursor.close()

    # Close the database connection
    conn.close()

    # Return the retrieved rows
    return rows