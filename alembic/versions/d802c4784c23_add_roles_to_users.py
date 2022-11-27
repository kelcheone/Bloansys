"""add roles to users

Revision ID: d802c4784c23
Revises: a3dde19a894d
Create Date: 2022-11-27 14:13:59.820198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd802c4784c23'
down_revision = 'a3dde19a894d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # add lables to users table the default role is user not null
    op.add_column('users', sa.Column('role', sa.String(50),
                  nullable=False, server_default='user'))


def downgrade() -> None:
    op.drop_column('users', 'role')
