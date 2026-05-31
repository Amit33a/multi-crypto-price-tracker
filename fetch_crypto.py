#Requests library send http request
import requests

#The function created for reusable logic
def fetch_crypto_price():

    #API URL 
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,binancecoin&vs_currencies=usd'

    #Handled request safely
    try:

       #Call API and GET Response
       response = requests.get(url,timeout=10)

       #Check status for API request
       response.raise_for_status()

       #Convert to JSON
       data = response.json()
       
 
       #Extract Data
       bitcoin_price = data.get("bitcoin", {}).get("usd")
       ethereum_price = data.get("ethereum", {}).get("usd")
       solana_price = data.get("solana", {}).get("usd")
       binancecoin_price = data.get("binancecoin", {}).get("usd")

       #Return price
       return {"bitcoin": bitcoin_price,
            "ethereum": ethereum_price,
            "solana": solana_price,
            "binancecoin": binancecoin_price
            }

#Handled request failure
    except requests.exceptions.RequestException as error:
        print(f"Error Type: {type(error).__name__}")
        print(f"Error Message: {error}")
        return None

