"""add user_id column to transactions

Revision ID: 6040c5265bac
Revises: 505218e4516f
Create Date: 2022-11-26 14:28:52.631180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6040c5265bac'
down_revision = '505218e4516f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add user id column to transactions table
    op.execute("ALTER TABLE transactions ADD COLUMN user_id INTEGER")
    op.execute(
        "ALTER TABLE transactions ADD FOREIGN KEY (user_id) REFERENCES users(user_id)")


def downgrade() -> None:
    op.execute("ALTER TABLE transactions DROP COLUMN user_id")
