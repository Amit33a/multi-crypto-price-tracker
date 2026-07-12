# Requests library sends HTTP requests
import requests

# Time module pauses execution between retries
import time

# Import application logger
from logger_config import logger

# Import timeout and retry
from config import REQUEST_TIMEOUT, MAX_RETRIES


# Fetch cryptocurrency prices from CoinGecko
def fetch_crypto_price() -> dict[str, float] | None:

    # CoinGecko API endpoint
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,binancecoin&vs_currencies=usd"

    # Attempt the request multiple times
    for attempt in range(1, MAX_RETRIES + 1):

        try:

            logger.info(f"API request to CoinGecko (Attempt {attempt}/{MAX_RETRIES})")

            # Send HTTP request
            response = requests.get(url, timeout=REQUEST_TIMEOUT)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Convert JSON response into Python dictionary
            data = response.json()

            logger.info("Successfully fetched cryptocurrency prices")

            # Extract cryptocurrency prices safely
            prices = {
                "bitcoin": data.get("bitcoin", {}).get("usd"),
                "ethereum": data.get("ethereum", {}).get("usd"),
                "solana": data.get("solana", {}).get("usd"),
                "binancecoin": data.get("binancecoin", {}).get("usd"),
            }

            # Find missing cryptocurrency prices
            missing_prices = [coin for coin, price in prices.items() if price is None]

            # Validate API response
            if missing_prices:

                logger.error(
                    f"Incomplete API response. Missing prices: {', '.join(missing_prices)}"
                )

                return None

            logger.info("Successfully fetched cryptocurrency prices")

            return prices

        # Handle invalid JSON responses
        except ValueError as error:

            logger.error(f"Invalid JSON response received: {error}")

            return None

        # Handle network-related errors
        except requests.exceptions.RequestException as error:

            logger.warning(f"Attempt {attempt} failed: {error}")

            print(f"Attempt {attempt} failed: {error}")

            # Stop retrying after the final attempt
            if attempt == MAX_RETRIES:

                logger.error(
                    "Maximum retry attempts reached. Unable to fetch cryptocurrency prices."
                )

                return None

            # Calculate exponential backoff delay
            delay = 2 ** (attempt - 1)

            logger.info(f"Waiting {delay} seconds before retrying...")

            time.sleep(delay)
