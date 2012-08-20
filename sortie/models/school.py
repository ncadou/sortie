"""Models various school elements.

Note: although the data models supports multiple schools, the rest of the
software package does not and assumes there is going to be only one.

"""

from colanderalchemy import Column
from sqlalchemy import ForeignKey, Integer, Unicode
from sqlalchemy.orm import backref, relationship

from . import TimestampedBase


class School(TimestampedBase):
    """Represents a school."""
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)


class Class(TimestampedBase):
    """A school class which has students."""
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)

    school_id = Column(Integer, ForeignKey('schools.id'), nullable=False)
    school = relationship('School', backref='classes')


class Student(TimestampedBase):
    """A person who attends a class at school."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)

    class_id = Column(Integer, ForeignKey('classes.id'), nullable=False)
    class_ = relationship('Class', backref='students')
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    person = relationship('Person', backref=backref('student', uselist=False))
