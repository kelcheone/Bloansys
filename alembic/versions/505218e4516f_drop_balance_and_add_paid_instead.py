"""drop balance and add paid instead

Revision ID: 505218e4516f
Revises: 4ec03a44feba
Create Date: 2022-11-26 11:33:50.805977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505218e4516f'
down_revision = '4ec03a44feba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # drop balance and add paid instead
    op.execute("ALTER TABLE loans DROP COLUMN balance")
    op.execute("ALTER TABLE loans ADD COLUMN paid FLOAT NOT NULL DEFAULT 0.0")


def downgrade() -> None:
    op.execute("ALTER TABLE loans DROP COLUMN paid")
    op.execute("ALTER TABLE loans ADD COLUMN balance FLOAT NOT NULL DEFAULT 0.0")
