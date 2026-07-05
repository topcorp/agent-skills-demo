---
name: log-search
description: Narrow a noisy log stream down to the events that explain an incident.
---

# Log Search

1. Start from the incident time window; widen only if needed.
2. Filter to the affected service and `level>=error`.
3. Group by error message / stack signature to find the dominant failure.
4. Pivot on a request/trace id from a representative error to see the full path.
