"""add if user column

Revision ID: de2f3e6d4a9d
Revises: 3c4f39bb29c2
Create Date: 2022-11-25 20:10:05.729396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de2f3e6d4a9d'
down_revision = '3c4f39bb29c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # add a column to the guarantors to table to indicate if a use is a custome.
    op.execute('''
    ALTER TABLE guarantors
    ADD COLUMN is_customer BOOLEAN NOT NULL DEFAULT FALSE;
    ''')


def downgrade() -> None:
    op.execute('''
    ALTER TABLE guarantors
    DROP COLUMN is_customer;
    ''')
