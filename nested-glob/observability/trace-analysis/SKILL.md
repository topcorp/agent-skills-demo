---
name: trace-analysis
description: Use distributed traces to find the slow span behind a latency regression.
---

# Trace Analysis

1. Pull a handful of slow traces for the affected endpoint from the tracing backend.
2. Find the span with the largest self-time (not just total time).
3. Correlate that span's service + operation with recent deploys or config changes.
4. Confirm the hypothesis on a second, independent slow trace before acting.
