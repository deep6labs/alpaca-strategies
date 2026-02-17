import requests
import os
from dotenv import load_dotenv
from pathlib import Path

def test_flipped_keys():
    # 1. Load the values currently in .env
    env_path = Path("/home/asha/repos/alpaca-strategies/.env")
    load_dotenv(dotenv_path=env_path)
    
    # These are the values as they currently exist in your .env
    val_a = os.getenv('ALPACA_PAPER_KEY_ID')
    val_b = os.getenv('ALPACA_PAPER_SECRET_KEY')
    
    url = "https://paper-api.alpaca.markets/v2/account"
    
    # CROSS-OVER TEST: Using Secret as ID and ID as Secret
    print("--- FLIPPED KEYS TEST ---")
    print(f"Using for ID: {val_b[:10]}...") # The 26-char string
    print(f"Using for SECRET: {val_a[:10]}...") # The 40-char string
    
    headers = {
        "APCA-API-KEY-ID": val_b,      # Current Secret used as ID
        "APCA-API-SECRET-KEY": val_a    # Current ID used as Secret
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            print("\nSUCCESS! Flipped keys worked. Updating .env now...")
            # I will only update the .env if this actually works
        else:
            print("\nRESULT: Still Unauthorized. Flipping did not resolve the issue.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_flipped_keys()
