"""Person-related models."""

from colanderalchemy import Column
from sqlalchemy import ForeignKey, Integer, Table, Unicode
from sqlalchemy.orm import relationship

from . import TimestampedBase

family_table = Table('family_associations', TimestampedBase.metadata,
    Column('parent_id', Integer, ForeignKey('people.id')),
    Column('child_id', Integer, ForeignKey('people.id'))
)


class Person(TimestampedBase):
    """A user that is also a person."""
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(128), nullable=False)
    last_name = Column(Unicode(128), nullable=False)
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
    user = relationship('User', uselist=False, backref='person')
    children = relationship('Person', secondary=family_table,
                            backref='parents',
                            primaryjoin=(id == family_table.c.parent_id),
                            secondaryjoin=(id == family_table.c.child_id))
