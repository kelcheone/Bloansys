"""create guarantor loan relationship

Revision ID: 3c4f39bb29c2
Revises: 8e8ff19256cb
Create Date: 2022-11-25 20:03:22.576919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c4f39bb29c2'
down_revision = '8e8ff19256cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add  a guarantor_id column to the loans table which is a foreign key to the guarantors table
    op.execute('''
    ALTER TABLE loans
    ADD COLUMN guarantor_id INTEGER REFERENCES guarantors(guarantor_id) ON DELETE CASCADE;
    ''')


def downgrade() -> None:
    op.execute('''
    ALTER TABLE loans
    DROP COLUMN guarantor_id;
    ''')
