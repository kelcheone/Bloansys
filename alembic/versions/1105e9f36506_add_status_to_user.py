"""add status to user

Revision ID: 1105e9f36506
Revises: 6040c5265bac
Create Date: 2022-11-26 21:24:21.680182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1105e9f36506'
down_revision = '6040c5265bac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add a status column to users table the default is unverfied.
    op.execute('''
        ALTER TABLE users
        ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'unverified';
    ''')


def downgrade() -> None:
    op.execute('''
        ALTER TABLE user
        DROP COLUMN status;
    ''')
