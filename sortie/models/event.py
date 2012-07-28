"""Models that deal with events."""

from colanderalchemy import Column
from sqlalchemy import Date, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship

from . import TimestampedBase


class Event(TimestampedBase):
    """An event in the system."""
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    description = Column(Unicode(1024), nullable=False)
    date = Column(Date)


class Registration(TimestampedBase):
    """Associates a person with an event."""
    __tablename__ = 'registrations'

    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    event = relationship('Event', backref='registrations')
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    person = relationship('Person', backref='registrations')
