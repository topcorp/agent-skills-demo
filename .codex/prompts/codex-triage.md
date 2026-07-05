---
name: codex-triage
description: A Codex-flavored skill living under a .codex path, used to verify agent_type inference reports "codex".
---

# Codex Triage

This skill sits under `.codex/prompts/`, so the importer's best-effort
`agent_type` inference should classify it as **codex** (display metadata only).

1. Reproduce the reported behavior locally.
2. Bisect recent changes to isolate the regressing commit.
3. Propose the minimal fix and a regression test.
