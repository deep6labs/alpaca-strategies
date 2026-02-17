# Independent Strategy Hypotheses Tracking

This document tracks multiple independent deterministic theories. Each is tested in parallel via virtual logging.

## [DET-1] Basis Arbitrage (Index/ETF)
- **Concept:** Capturing tracking errors between highly correlated sector ETFs (e.g., SPY vs IVV) or stock-future basis.
- **Certainty Factor:** High (Mathematical convergence).
- **Status:** Idle - Scanning for >0.05% divergence windows.

## [DET-2] Dividend Capture with Perfect Hedge
- **Concept:** Buying on the day before ex-dividend and simultaneously shorting equivalent value in a highly correlated but non-paying instrument or using options to lock in the dividend amount while neutralizing price movement.
- **Certainty Factor:** Medium-High (Requires precise timing and cost analysis).
- **Status:** Drafting data pull for upcoming ex-dividend dates.

## [DET-3] Corporate Action Arbitrage
- **Concept:** Exploiting fixed-price cash mergers or tender offers where the legal framework guarantees a final price, trading the "deal spread" when risk is near-zero.
- **Certainty Factor:** Very High (Legal/Contractual guarantee).
- **Status:** Monitoring M&A news feeds via web_search.

## [DET-4] Passive Flow Front-Running (Mandated)
- **Concept:** Index additions/deletions. When an index like the S&P 500 adds a ticker, massive passive funds *must* buy on a specific date.
- **Certainty Factor:** High (Mandated buy volume).
- **Status:** Checking upcoming index change announcements.
