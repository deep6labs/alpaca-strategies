import os
import requests
from pathlib import Path

def test_raw_env():
    # Use the shared .env file
    env_path = Path("/home/asha/.env")
    print(f"Reading from: {env_path}")
    
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
    
    # Try different Paper endpoints
    endpoints = [
        "https://paper-api.alpaca.markets/v2/account",
        "https://paper-api.alpaca.markets/v2/clock"
    ]

    print(f"Key ID: {key_id}")
    # I will not print the full secret for safety, but checking its length
    print(f"Secret Length: {len(secret) if secret else 0}")

    for url in endpoints:
        print(f"\nTesting URL: {url}")
        headers = {
            "APCA-API-KEY-ID": key_id,
            "APCA-API-SECRET-KEY": secret
        }

        try:
            response = requests.get(url, headers=headers)
            print(f"Status: {response.status_code}")
            print(f"Body: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_raw_env()
