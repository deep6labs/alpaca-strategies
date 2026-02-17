# Alpaca Strategies

Repository for developing, testing, and tracking algorithmic trading strategies using the Alpaca.markets API.

## Project Structure
- `strategies/`: Core algorithmic logic.
- `research/`: Jupyter notebooks and backtesting results.
- `logs/`: (Gitignored) Local execution logs for paper trading.
- `config/`: Configuration templates (secrets managed via .env).

## Workflow
1. **Research:** Define Alpha in `research/`.
2. **Backtest:** Validate against historical data.
3. **Paper Trade:** Deploy to `https://paper-api.alpaca.markets`.
4. **Monitor:** Track performance vs. benchmarks.

## Setup
```bash
# Clone
git clone https://github.com/deep6labs/alpaca-strategies.git
cd alpaca-strategies

# Install dependencies
pip install alpaca-py python-dotenv
```

## Maintenance
Managed by Asha. Status updates synced to [Boardroom](https://github.com/deep6labs/boardroom).
