"""add created_at column to loans

Revision ID: 4ec03a44feba
Revises: de2f3e6d4a9d
Create Date: 2022-11-26 10:58:21.373170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ec03a44feba'
down_revision = 'de2f3e6d4a9d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add a created_at column to the loans table
    op.execute('''
    ALTER TABLE loans
    ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
    ''')


def downgrade() -> None:
    op.execute('''
    ALTER TABLE loans
    DROP COLUMN created_at;
    ''')
