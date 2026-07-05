---
name: rollback
description: Roll a service back to the previous known-good release when a deploy regresses.
---

# Rollback a Deploy

When a fresh deploy causes errors, roll back first and investigate second.

1. Identify the previous known-good image tag / release SHA.
2. Trigger the rollback (redeploy the prior tag or `kubectl rollout undo`).
3. Watch error-rate and latency return to baseline.
4. Freeze further deploys to this service until root cause is understood.
