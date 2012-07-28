<%
    def indent(text, indents=1):
        return '\n'.join([('    ' * indents + l) for l in text.split('\n')])

%>"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision}
Create Date: ${create_date}

"""

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}

from alembic import context, op
import sqlalchemy as sa
import transaction
${imports if imports else ''}

from sortie import models as m
from sortie.lib import config

db = m.DBSession


def upgrade(pyramid_env):
    with context.begin_transaction():
    ${indent(upgrades if upgrades else 'pass')}

    # Do stuff with the app's models here.
    with transaction.manager:
        pass


def downgrade(pyramid_env):
    with context.begin_transaction():
    ${indent(downgrades if downgrades else 'pass')}
