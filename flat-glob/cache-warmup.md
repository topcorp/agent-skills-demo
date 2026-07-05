---
name: cache-warmup
description: Warm the CDN and application caches after a cold deploy or cache flush to avoid a thundering-herd on origin.
---

# Cache Warm-up

After a cache flush or cold start, prime caches before shifting full traffic.

1. Replay the top-N request URLs from the last hour against the new fleet.
2. Watch origin request rate — keep it under the origin's safe threshold.
3. Ramp traffic 10% → 50% → 100% while cache hit-ratio climbs back above 90%.
4. Abort and roll back the traffic shift if origin error-rate spikes.
