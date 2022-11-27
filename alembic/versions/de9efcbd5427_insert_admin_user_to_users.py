"""insert admin user to users

Revision ID: de9efcbd5427
Revises: 65ff0a8e7922
Create Date: 2022-11-27 22:12:51.365412

"""
from alembic import op
import sqlalchemy as sa

from src.utils import hash_password


# revision identifiers, used by Alembic.
revision = 'de9efcbd5427'
down_revision = '65ff0a8e7922'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # hash password and make it string
    hashed = str(hash_password('admin'))
    op.execute(f'''
    INSERT INTO users (first_name, last_name, password, email, national_id, status, role, phone_number) VALUES ('admin', 'admin',  '{hashed}', 'admin@admin.com', '123456789', 'verified', 'admin', '123456789');
    '''
               )


def downgrade() -> None:
    pass
