"""Some utilities for working with SQLAlchemy."""

from datetime import datetime
import sys

from colanderalchemy import Column, SQLAlchemyMapping
from sqlalchemy import DateTime, engine_from_config, event, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
from sqlalchemy.orm.util import has_identity
from zope.sqlalchemy import ZopeTransactionExtension

from pyramid.paster import get_appsettings, setup_logging


def declarative_bases(metadata):
    """Return all declarative bases bound to a single metadata object."""
    registry = dict()
    return (declarative_base(metadata=metadata, class_registry=registry),
            declarative_base(cls=Timestamped, class_registry=registry,
                             metadata=metadata))


def create_engine(config_uri):
    """Return an SQLAlchemy engine configured as per the provided config."""
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    return engine


class BaseOps(object):
    """Basic database operations are abstracted away in this class.

    The idea is to have the API as independent as practically possible from
    both data storage- and web- specific stuff.

    """
    def __iter__(self, **kwargs):
        """Return a generator that iterates through model columns."""
        return self.iteritems(**kwargs)

    def iteritems(self, include=None, exclude=None):
        """Return a generator that iterates through model columns.

        Fields iterated through can be specified with include/exclude.

        """
        if include is not None and exclude is not None:
            include = set(include) - set(exclude)
            exclude = None
        for c in self.__table__.columns:
            if ((not include or c.name in include)
            and (not exclude or c.name not in exclude)):
                yield(c.name, getattr(self, c.name))

    @classmethod
    def validator(cls, mapping_cls=None, include=None, exclude=None):
        """Return a ColanderAlchemy schema mapper.

        Fields targeted by the validator can be specified with include/exclude.

        """
        if include == '__nopk__':
            includes = cls._col_names() - cls._pk_names()
        elif include == '__pk__':
            includes = cls._pk_names()
        elif include is None:
            includes = cls._col_names()
        else:
            includes = set(include)
        if exclude is not None:
            includes -= set(exclude)

        if mapping_cls is None:
            mapping_cls = SQLAlchemyMapping
        return mapping_cls(cls, includes=list(includes))

    @classmethod
    def _col_names(cls):
        return set(cls.__table__.c.keys())

    @classmethod
    def _pk_names(cls):
        return set(cls.__table__.primary_key.columns.keys())

    @property
    def is_new(self):
        return not has_identity(self)

    @classmethod
    def create(cls, obj=None, flush=False, **values):
        if obj is None:
            obj = cls(**values)
        else:
            obj.update(**values)
        obj.save(flush)
        return obj

    @classmethod
    def get(cls, **criteria):
        return DBSession.query(cls).filter_by(**criteria).one()

    @classmethod
    def list(cls, **criteria):
        return DBSession.query(cls).filter_by(**criteria).all()

    def delete(self):
        DBSession.delete(self)

    def update(self, **values):
        fields = self._col_names()
        for name, value in values.iteritems():
            if name in fields:
                setattr(self, name, value)

    def save(self, flush=False):
        if self.is_new:
            DBSession.add(self)
        if flush:
            DBSession.flush()

    @classmethod
    def inject_api(cls, name):
        """Inject common methods in a API module."""
        for attr in 'create', 'get', 'list', 'validator':
            setattr(sys.modules[name], attr, getattr(cls, attr))


class Timestamped(BaseOps):
    """An automatically timestamped mixin."""
    ins_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    mod_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    _stamps = ['ins_date', 'mod_date']

    def iteritems(self, include=None, exclude=None):
        if exclude is None:
            exclude = self._stamps
        elif len(exclude) > 0:
            exclude = set(exclude) | set(self._stamps)
        return super(Timestamped, self).iteritems(exclude=exclude,
                                                  include=include)

    @classmethod
    def validator(cls, exclude=None, **kwargs):
        """Return a ColanderAlchemy schema mapper.

        Fields targeted by the validator can be specified with include/exclude.

        """
        if exclude is None:
            exclude = cls._stamps
        elif len(exclude) > 0:
            exclude = set(exclude) | set(cls._stamps)
        kwargs['exclude'] = exclude
        return super(Timestamped, cls) \
                .validator(mapping_cls=TimestampedSQLAlchemyMapping, **kwargs)


class TimestampedSQLAlchemyMapping(SQLAlchemyMapping):
    """The ColanderAlchemy schema mapper for TimestampedBase."""
    def __init__(self, cls, excludes=None, **kwargs):
        stamps = ['ins_date', 'mod_date']
        if excludes is None:
            excludes = stamps
        elif len(excludes) > 0:
            excludes = set(excludes) | set(stamps)
        parent = super(TimestampedSQLAlchemyMapping, self)
        return parent.__init__(cls, excludes=excludes, **kwargs)


def insert_timestamp(mapper, connection, target):
    """Initialize timestamps on models that have these fields.

    Event handler for 'before_insert'.

    """
    timestamp = datetime.utcnow()
    if hasattr(target, 'ins_date'):
        target.ins_date = timestamp
    if hasattr(target, 'mod_date'):
        target.mod_date = timestamp


def update_timestamp(mapper, connection, target):
    """Update the modified date on models that have this field.

    Event handler for 'before_update'.

    """
    if hasattr(target, 'mod_date'):
        target.mod_date = datetime.utcnow()


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

metadata = MetaData()
Base, TimestampedBase = declarative_bases(metadata)

event.listen(mapper, 'before_insert', insert_timestamp)
event.listen(mapper, 'before_update', update_timestamp)


def includeme(config):
    """Initialize SQLAlchemy at app start-up time."""
    engine = engine_from_config(config.registry.settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
