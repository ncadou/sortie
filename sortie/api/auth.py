"""Authentication-related API calls."""

from cryptacular.bcrypt import BCRYPTPasswordManager

MANAGER = BCRYPTPasswordManager()


def authenticate_user(user, password):
    """Authenticate a user using a username and password."""
    return MANAGER.check(user.password, password)
