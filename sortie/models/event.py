"""Models that deal with events."""

from colanderalchemy import Column
from sqlalchemy import (Boolean, Date, Enum, ForeignKey, Integer, Numeric,
                        Table, Unicode)
from sqlalchemy.orm import relationship

from . import TimestampedBase

# Association table between events and classes.
event_classes = Table('event_classes', TimestampedBase.metadata,
                      Column('event_id', Integer, ForeignKey('events.id')),
                      Column('class_id', Integer, ForeignKey('classes.id')))


class Event(TimestampedBase):
    """An event in the system."""
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    description = Column(Unicode(1024), nullable=False)
    date = Column(Date)

    classes = relationship('Class', secondary=event_classes, backref='events')

    def __contains__(self, person):
        """Check if a person is registered."""
        for reg in person.registrations:
            if reg.active and reg.event == self:
                return True

    def has_person(self, person):
        """Check if a person is registered."""
        for reg in person.registrations:
            if reg.active and reg.event == self:
                return True

        return False


class Registration(TimestampedBase):
    """Associates a person with an event."""
    __tablename__ = 'registrations'

    active = Column(Boolean, nullable=False, default=True)

    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    event = relationship('Event', backref='registrations')
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    person = relationship('Person', backref='registrations')


_event_option_types = (u'checkbox', u'date', u'decimal', u'int', u'radio',
                       u'text')


class EventOption(TimestampedBase):
    """Represent an option specific to an event."""
    __tablename__ = 'event_options'

    id = Column(Integer, primary_key=True)
    description = Column(Unicode(1024), nullable=False)
    name = Column(Unicode(128), nullable=False)
    type = Column(Enum(*_event_option_types, name='event_option_types'))
    price = Column(Numeric(2))

    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    event = relationship('Event', backref='options')


class EventOptionRegistration(TimestampedBase):
    """Associates a person with an event option."""
    __tablename__ = 'event_option_registrations'

    value = Column(Unicode(128), nullable=False)

    event_option_id = Column(Integer, ForeignKey('event_options.id'),
                             primary_key=True)
    event_option = relationship('EventOption', backref='registrations')
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    person = relationship('Person', backref='event_options')
