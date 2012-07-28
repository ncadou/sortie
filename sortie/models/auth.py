"""Authentication-related models."""

from colanderalchemy import Column
from sqlalchemy import Integer, String

from . import TimestampedBase


class User(TimestampedBase):
    """A user in the system."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
