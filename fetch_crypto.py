# Requests library sends HTTP requests
import requests

# Time module pauses execution between retries
import time

# Import application logger
from logger_config import logger


# Fetch cryptocurrency prices from CoinGecko
def fetch_crypto_price():

    # CoinGecko API endpoint
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,binancecoin&vs_currencies=usd"
    

    # Maximum retry attempts
    max_retries = 3

    # Attempt the request multiple times
    for attempt in range(1, max_retries + 1):

        try:

            logger.info(f"API request to CoinGecko (Attempt {attempt}/{max_retries})")

            # Send HTTP request
            response = requests.get(url, timeout=10)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Convert JSON response into Python dictionary
            data = response.json()

            logger.info("Successfully fetched cryptocurrency prices")

            # Return cryptocurrency prices safely
            return {
                "bitcoin": data.get("bitcoin", {}).get("usd"),
                "ethereum": data.get("ethereum", {}).get("usd"),
                "solana": data.get("solana", {}).get("usd"),
                "binancecoin": data.get("binancecoin", {}).get("usd"),
            }

        except requests.exceptions.RequestException as error:

            logger.warning(f"Attempt {attempt} failed: {error}")

            print(f"Attempt {attempt} failed: {error}")

            # Stop retrying after the final attempt
            if attempt == max_retries:

                logger.error("Maximum retry attempts reached. Unable to fetch cryptocurrency prices.")

                return None

            # Wait before the next retry
            time.sleep(2)