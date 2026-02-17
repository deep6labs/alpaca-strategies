import os
import requests
from pathlib import Path

def test_raw_env():
    env_path = Path("/home/asha/repos/alpaca-strategies/.env")
    print(f"Reading from: {env_path}")
    
    # Manually parsing to be 100% sure what we are sending
    lines = env_path.read_text().splitlines()
    env_data = {}
    for line in lines:
        if "export " in line:
            line = line.replace("export ", "")
        if "=" in line and not line.startswith("#"):
            key, val = line.split("=", 1)
            env_data[key.strip()] = val.strip()

    key_id = env_data.get('ALPACA_PAPER_KEY_ID')
    secret = env_data.get('ALPACA_PAPER_SECRET_KEY')
    # Force the base URL to V2 account endpoint
    base_url = "https://paper-api.alpaca.markets/v2/account"

    print(f"Key ID (first 5): {key_id[:5] if key_id else 'None'}")
    print(f"Secret (first 2): {secret[:2] if secret else 'None'}")

    headers = {
        "APCA-API-KEY-ID": key_id,
        "APCA-API-SECRET-KEY": secret
    }

    try:
        response = requests.get(base_url, headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Body: {response.text}")
        
        if response.status_code == 200:
            print("SUCCESS: Authenticated successfully.")
        else:
            print("FAILURE: Header or Key mismatch.")
            
    except Exception as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    test_raw_env()
