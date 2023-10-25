"""Add Role Column to User Table

Revision ID: 8a70b396c554
Revises: 
Create Date: 2023-10-11 13:06:56.465972

"""
from alembic import op
import sqlalchemy as sa
from enum import Enum
from sqlalchemy.sql import table

# revision identifiers, used by Alembic.
revision = '8a70b396c554'
down_revision = None
branch_labels = None
depends_on = None


class Role(Enum):
    ADMIN = 1
    USER = 2


def upgrade():
    op.add_column(
        'user_master',
        sa.Column('role',
                  sa.String(10),
                  nullable=False))

    user_master = table(
        'user_master',
        sa.Column('role', sa.VARCHAR(length=10))
    )

    op.execute(
        user_master
        .update()
        .values({'role': 'USER'})
    )


def downgrade():
    op.drop_column('user_master', 'role')
