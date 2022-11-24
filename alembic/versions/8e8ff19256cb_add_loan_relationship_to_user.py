"""add loan relationship to user

Revision ID: 8e8ff19256cb
Revises: bbf2815b8774
Create Date: 2022-11-24 13:34:46.367139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e8ff19256cb'
down_revision = 'bbf2815b8774'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # add loan relationship to user
    op.execute('''
    ALTER TABLE users
    ADD COLUMN loan_id INTEGER REFERENCES loans(loan_id) ON DELETE CASCADE;
    ''')


def downgrade() -> None:
    op.execute('''
    ALTER TABLE users
    DROP COLUMN loan_id;
    ''')
