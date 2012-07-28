"""bootstrap migration

Revision ID: 469b2546bfe1
Revises: None
Create Date: 2012-07-28 13:34:09.304262

"""

# revision identifiers, used by Alembic.
revision = '469b2546bfe1'
down_revision = None

from alembic import context, op
import sqlalchemy as sa
import transaction


from sortie import models as m
from sortie.lib import config

db = m.DBSession


def upgrade(pyramid_env):
    with context.begin_transaction():
        pass

    # Do stuff with the app's models here.
    with transaction.manager:
        pass


def downgrade(pyramid_env):
    with context.begin_transaction():
        pass
