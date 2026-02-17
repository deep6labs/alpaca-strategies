import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.common.exceptions import APIError

def verify_setup():
    # Load environment variables from the .env file in the current directory
    load_dotenv()
    
    # api_key = os.getenv('ALPACA_PAPER_KEY_ID')
    # secret_key = os.getenv('ALPACA_PAPER_SECRET_KEY')
    # base_url = os.getenv('ALPACA_PAPER_BASE_URL', 'https://paper-api.alpaca.markets')
    
    # Try direct environment variables first (already loaded in the shell/env)
    api_key = os.environ.get('ALPACA_PAPER_KEY_ID')
    secret_key = os.environ.get('ALPACA_PAPER_SECRET_KEY')
    base_url = os.environ.get('ALPACA_PAPER_BASE_URL', 'https://paper-api.alpaca.markets')

    if not api_key or not secret_key:
        print("Error: Missing credentials in .env file.")
        return

    try:
        # Initialize the client. paper=True ensures we use the paper endpoint.
        client = TradingClient(api_key, secret_key, paper=True)
        account = client.get_account()
        
        print("--- Alpaca Connection Verified ---")
        print(f"Account #:      {account.account_number}")
        print(f"Status:         {account.status}")
        print(f"Currency:       {account.currency}")
        print(f"Buying Power:   ${account.buying_power}")
        print(f"Cash:           ${account.cash}")
        print(f"Equity:         ${account.equity}")
        print(f"Multiplier:     {account.multiplier}")
        print("---------------------------------")
        
    except APIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    verify_setup()
