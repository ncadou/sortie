"""Various helpers to use in templates."""

from ..api import school


def schoolname():
    """Return the current school name."""
    return school.find()[0].name
