"""add column status to loans

Revision ID: a3dde19a894d
Revises: 1105e9f36506
Create Date: 2022-11-26 21:40:16.329794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3dde19a894d'
down_revision = '1105e9f36506'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "ALTER TABLE loans ADD COLUMN status VARCHAR(255) NOT NULL DEFAULT 'pending'")


def downgrade() -> None:
    op.execute("ALTER TABLE loans DROP COLUMN status")
