"""Authentication-related models."""

from colanderalchemy import Column
from sqlalchemy import Integer, Unicode

from . import TimestampedBase


class User(TimestampedBase):
    """A user in the system."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(128), nullable=False)
    password = Column(Unicode(128), nullable=False)
