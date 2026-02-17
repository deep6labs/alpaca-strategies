import requests
import os
from dotenv import load_dotenv
from pathlib import Path

def debug_alpaca_call():
    # 1. Load from the specific .env file
    env_path = Path("/home/asha/repos/alpaca-strategies/.env")
    load_dotenv(dotenv_path=env_path)
    
    # 2. Extract values
    key_id = os.getenv('ALPACA_PAPER_KEY_ID')
    secret_key = os.getenv('ALPACA_PAPER_SECRET_KEY')
    
    # 3. Setting the Paper Endpoint
    # Note: /v2/account is the standard endpoint to check account info
    url = "https://paper-api.alpaca.markets/v2/account"
    
    # 4. Constructing Headers
    # These are the TWO EXACT HEADERS Alpaca requires
    headers = {
        "APCA-API-KEY-ID": key_id,
        "APCA-API-SECRET-KEY": secret_key
    }
    
    print(f"--- DEBUG CALL DETAILS ---")
    print(f"Target URL: {url}")
    print(f"Header 1 (Name): APCA-API-KEY-ID")
    print(f"Header 1 (Value): {key_id}")
    print(f"Header 2 (Name): APCA-API-SECRET-KEY")
    print(f"Header 2 (Value): {secret_key}")
    print(f"--------------------------\n")
    
    # 5. Make the request
    try:
        response = requests.get(url, headers=headers)
        print(f"HTTP Status Code: {response.status_code}")
        print(f"Raw Response Body: {response.text}")
        
        if response.status_code == 401:
            print("\nRESULT: 401 Unauthorized. This usually means the Key ID is wrong, the Secret is wrong, or the Key ID does not belong to the Paper environment.")
        elif response.status_code == 200:
            print("\nRESULT: Success! Authentication works.")
            
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    debug_alpaca_call()
