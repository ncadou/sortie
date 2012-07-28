"""Models related to a school."""

from colanderalchemy import Column
from sqlalchemy import ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship

from . import TimestampedBase


class Class(TimestampedBase):
    """A school class which has students."""
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)


class Student(TimestampedBase):
    """A person who attends a class at school."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)

    class_id = Column(Integer, ForeignKey('classes.id'), nullable=False)
    class_ = relationship('Class', backref='student')
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    person = relationship('Person', uselist=False, backref='student')
