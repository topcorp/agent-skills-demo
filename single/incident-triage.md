---
name: incident-triage
description: First-response triage checklist for a production incident — assess blast radius, declare severity, and page the right owners.
allowed-tools: Bash, Read
---

# Incident Triage

When an alert fires and you are first on the scene, work this checklist top to bottom.

## 1. Confirm the signal is real
- Open the firing alert and check the underlying metric/log query.
- Rule out a synthetic/probe alert or a known maintenance window.

## 2. Assess blast radius
- Is it one service, one region, or global?
- Are customers impacted, or is this internal-only?

## 3. Declare severity
- **SEV1** — customer-facing outage or data loss.
- **SEV2** — degraded experience, partial outage.
- **SEV3** — internal or single-tenant impact.

## 4. Page the owners
- Page the on-call for the owning service.
- For SEV1/SEV2, open an incident channel and post the initial summary.
