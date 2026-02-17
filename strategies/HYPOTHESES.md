# Independent Strategy Hypotheses Tracking

This document tracks multiple independent deterministic theories. Each is tested in parallel via virtual logging.

## [DET-1] Basis Arbitrage (Index/ETF)
- **Concept:** Capturing tracking errors between highly correlated sector ETFs.
- **Certainty Factor:** LOW (Invalidated by QA).
- **Status:** DISCARDED. Reason: Lack of atomic execution in retail APIs and IEX data latency makes this a high-risk probabilistic trade, not deterministic.

## [DET-2] Dividend Capture with Perfect Hedge
- **Concept:** Buying before ex-dividend and shorting a correlated instrument.
- **Certainty Factor:** LOW (Invalidated by QA).
- **Status:** DISCARDED. Reason: Shorting the stock makes one liable for the dividend payment (net-zero), and option spreads eat the entire yield via bid/ask slippage.

## [DET-5] Index Addition Front-Running (Event-Driven)
- **Concept:** Buying S&P 500 additions between the announcement and effective dates.
- **Certainty Factor:** High (Mandated buy volume).
- **Status:** Monitoring for March Quarterly Rebalance Announcement (expected late Feb/early March).

## [DET-3] Corporate Action Arbitrage
- **Concept:** Exploiting fixed-price cash mergers or tender offers where the legal framework guarantees a final price, trading the "deal spread" when risk is near-zero.
- **Certainty Factor:** Very High (Legal/Contractual guarantee).
- **Status:** Monitoring M&A news feeds via web_search.

## [DET-4] Passive Flow Front-Running (Mandated)
- **Concept:** Index additions/deletions. When an index like the S&P 500 adds a ticker, massive passive funds *must* buy on a specific date.
- **Certainty Factor:** High (Mandated buy volume).
- **Status:** Checking upcoming index change announcements.
