import os
import requests
from alpaca.trading.client import TradingClient

# Values from your .env
API_KEY = "8fT9..." # I will not write the full key here, but I will use os.environ
SECRET_KEY = "PK..."

def manual_test():
    api_key = os.environ.get('ALPACA_PAPER_KEY_ID')
    secret_key = os.environ.get('ALPACA_PAPER_SECRET_KEY')
    base_url = "https://paper-api.alpaca.markets/v2/account" # Try direct V2 path
    
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key
    }
    
    # Try direct REST call without SDK first to isolate
    response = requests.get(base_url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    manual_test()
