---
name: dns-debug
description: Diagnose DNS resolution failures between services in the cluster.
---

# DNS Debugging

1. Reproduce: `dig`/`nslookup` the failing name from an affected pod.
2. Check the resolver config (`/etc/resolv.conf`, CoreDNS/kube-dns health).
3. Look for recent changes to Services, NetworkPolicies, or the DNS ConfigMap.
4. Verify upstream resolvers are reachable and not rate-limiting.
