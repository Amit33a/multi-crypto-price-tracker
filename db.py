# Import PostgreSQL adapter to connect Python with PostgreSQL database
import psycopg2

# Import database configuration values
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

# Import application logger
from logger_config import logger


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

    try:
        logger.info("Creating database table")

        with get_connection() as conn:

            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS multi_crypto_price (
                    id SERIAL PRIMARY KEY,
                    crypto_name VARCHAR(50) NOT NULL,
                    price_usd NUMERIC(18,8) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            logger.info("Database table created successfully")

    except Exception as e:

        logger.error(f"Error creating table: {e}")

        print(f"Error creating table: {e}")

    finally:
        cur.close()


# Insert a cryptocurrency price into the database
def insert_price(name: str, price: float) -> None:

    try:
        logger.info(f"Inserting {name} price into database")

        with get_connection() as conn:

            cur = conn.cursor()

            cur.execute("""
                INSERT INTO multi_crypto_price (crypto_name, price_usd)
                VALUES (%s, %s)
            """, (name, price))

            logger.info(f"Successfully inserted {name} price")

    except Exception as e:

        logger.error(f"Error inserting {name} price: {e}")

        print(f"Error inserting price: {e}")

    finally:
        cur.close()


# Retrieve all cryptocurrency prices from the database
def get_all_prices():

    try:
        logger.info("Retrieving cryptocurrency prices from database")

        with get_connection() as conn:

            cur = conn.cursor()

            cur.execute(
                "SELECT * FROM multi_crypto_price ORDER BY created_at DESC"
            )

            rows = cur.fetchall()

            logger.info(f"Retrieved {len(rows)} records from database")

            return rows

    except Exception as e:

        logger.error(f"Error getting prices: {e}")

        print(f"Error getting prices: {e}")

        return []

    finally:
        cur.close()