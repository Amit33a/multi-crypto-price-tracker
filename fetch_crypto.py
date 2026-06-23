# Requests library sends HTTP requests
import requests

# Import application logger
from logger_config import logger


# Function created for reusable logic
def fetch_crypto_price():

    # API URL
    url = (
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,binancecoin&vs_currencies=usd"
    )

    try:

        # Log API request start
        logger.info("Fetching cryptocurrency prices from CoinGecko API")

        # Call API and GET response
        response = requests.get(url, timeout=10)

        # Check HTTP status code
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Log successful API response
        logger.info("Successfully fetched cryptocurrency prices")

        # Return crypto prices safely
        return {
            "bitcoin": data.get("bitcoin", {}).get("usd"),
            "ethereum": data.get("ethereum", {}).get("usd"),
            "solana": data.get("solana", {}).get("usd"),
            "binancecoin": data.get("binancecoin", {}).get("usd"),
        }

    except requests.exceptions.RequestException as error:

        # Log API failure
        logger.error(f"Failed to fetch crypto prices: {error}")

        print(f"Error Type: {type(error).__name__}")
        print(f"Error Message: {error}")

        return None