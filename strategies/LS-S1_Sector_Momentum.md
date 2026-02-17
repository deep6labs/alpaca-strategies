# LS-S1: Sector Momentum / Mean Reversion

**Status:** Ideation

### 1. Hypothesis
Market dispersion often leaves individual sectors overextended or oversold relative to the benchmark. A dollar-neutral long-short portfolio can capture the "catch-up" effect while mitigating overall market risk (beta).

### 2. Selection Logic
- **Long Basket:** Top 5 stocks in the strongest sector (by 1-week momentum) that have the lowest 1-month RSI (mean reversion candidates within a strong trend).
- **Short Basket:** Top 5 stocks in the weakest sector that have the highest 1-month RSI.

### 3. Execution Logic
- **Interval:** Weekly rebalancing (Monday market open).
- **Weighting:** Equal-weighted (10% per position).
- **Universe:** S&P 500 constituents (high liquidity).

### 4. Risk Parameters
- **Max Position Size:** 10%
- **Portfolio Beta:** Target ~0.0 (Beta-Neutral).
- **Stop Loss:** 5% per individual leg.
