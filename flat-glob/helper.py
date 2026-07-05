# Not a skill — a helper script that lives alongside the skills.
# The importer must SKIP this under a *.md glob and emit a warning,
# because only .md files are imported.


def compute_error_budget(slo: float, window_days: int) -> float:
    """Return the allowed error minutes for an SLO over a window."""
    return (1.0 - slo) * window_days * 24 * 60
