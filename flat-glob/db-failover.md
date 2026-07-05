---
name: db-failover
description: Promote a read replica to primary when the primary Postgres instance is unhealthy.
---

# Database Failover

Use when the primary Postgres is unreachable or failing health checks.

1. Confirm the primary is truly down (not a network partition) via the cloud console.
2. Identify the most-caught-up replica (`SELECT * FROM pg_stat_replication`).
3. Promote it: `pg_ctl promote` (or the managed-DB failover button).
4. Repoint the writer endpoint / update the connection secret.
5. Verify writes succeed and replication re-forms on the remaining replicas.
6. File a follow-up to rebuild the demoted node.
