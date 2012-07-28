"""Person-related models."""

from colanderalchemy import Column
from sqlalchemy import ForeignKey, Integer, Unicode
from sqlalchemy.orm import backref, relationship

from . import TimestampedBase


class Person(TimestampedBase):
    """A user that is also a person."""
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(128), nullable=False)
    last_name = Column(Unicode(128), nullable=False)
    address = Column(Unicode(1024))
    city = Column(Unicode(128))
    postal_code = Column(Unicode(16))
    country = Column(Unicode(128))
    phone = Column(Unicode(32))
    email = Column(Unicode(128))

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', uselist=False, backref='person')
    children = relationship('Person', backref=backref('parent',
                                                      remote_side=[id]))
