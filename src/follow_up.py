"""Identify support requests that have reached the follow-up deadline."""


def needs_follow_up(age_hours):
    """Return True once the request is at least 24 hours old."""
    return age_hours >= 24
