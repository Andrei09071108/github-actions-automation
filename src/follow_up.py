"""Identify support requests that have reached the follow-up deadline."""


def needs_follow_up(age_hours, limit_hours=24):
    """Return True once the request is at least the configured age."""
    return age_hours > limit_hours
