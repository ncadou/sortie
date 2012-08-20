"""Person-related models."""

from colanderalchemy import Column
from sqlalchemy import Enum, ForeignKey, Integer, Table, Unicode, func, or_
from sqlalchemy.orm import backref, relationship

from . import TimestampedBase

family_table = Table('family_associations', TimestampedBase.metadata,
    Column('parent_id', Integer, ForeignKey('people.id')),
    Column('child_id', Integer, ForeignKey('people.id')))


class Person(TimestampedBase):
    """A user that is also a person."""
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(128), nullable=False)
    last_name = Column(Unicode(128), nullable=False)
    gender = Column(Enum('male', 'female', 'other', name='gender'))
    address = Column(Unicode(1024))
    city = Column(Unicode(128))
    state = Column(Unicode(128))
    postal_code = Column(Unicode(16))
    country = Column(Unicode(128))
    home_phone = Column(Unicode(32))
    work_phone = Column(Unicode(32))
    cell_phone = Column(Unicode(32))
    email = Column(Unicode(128))

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref=backref('person', uselist=False))
    children = relationship('Person', secondary=family_table,
                            backref='parents',
                            primaryjoin=(id == family_table.c.parent_id),
                            secondaryjoin=(id == family_table.c.child_id))

    @property
    def fullname(self):
        return ' '.join([self.first_name, self.last_name])

    @classmethod
    def by_name(cls, name):
        """Get a person by name."""
        fname, lname = name.lower().split(' ')
        q = cls.db().query(Person)
        q = q.filter(func.lower(Person.first_name) == fname)
        return q.filter(func.lower(Person.last_name) == lname).one()

    @classmethod
    def complete(cls, name):
        """Return poor man's possible matches from the provided name."""
        criteria = []
        for part in name.split(' '):
            criteria.append(Person.first_name.ilike(u'%%%s%%' % part))
            criteria.append(Person.last_name.ilike(u'%%%s%%' % part))
        return cls.db().query(Person).filter(or_(*criteria))
