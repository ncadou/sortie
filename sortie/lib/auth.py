"""Authentication-related utility functions."""

from cryptacular.bcrypt import BCRYPTPasswordManager

MANAGER = BCRYPTPasswordManager()


def encode_password(password):
    """Return hashed version of password."""
    return str(MANAGER.encode(password))
