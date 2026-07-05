# Kubernetes Pod Crash Loop

This skill file intentionally has **no YAML frontmatter**, so the importer must
derive the skill name from the filename (`no-frontmatter`) and the title from
this first H1 heading.

## Steps

1. `kubectl describe pod <pod>` — read the last state and exit code.
2. Check `kubectl logs <pod> --previous` for the crash reason.
3. Common causes: bad config/secret, failed readiness probe, OOMKilled (exit 137).
4. Fix the underlying config and let the Deployment roll the pod.
