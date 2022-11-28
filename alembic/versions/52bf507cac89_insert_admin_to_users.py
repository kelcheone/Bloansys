"""insert admin to users

Revision ID: 52bf507cac89
Revises: d802c4784c23
Create Date: 2022-11-28 13:59:17.951159

"""
from alembic import op
import sqlalchemy as sa
from src.utils import hash_password


# revision identifiers, used by Alembic.
revision = '52bf507cac89'
down_revision = 'd802c4784c23'
branch_labels = None
depends_on = None


def upgrade() -> None:
    hashed = str(hash_password('admin'))
    op.execute(f'''
    INSERT INTO users (first_name, last_name, password, email, national_id, status, role, phone_number) VALUES ('admin', 'admin',  '{hashed}', 'admin@admin.com', '123456789', 'verified', 'admin', '123456789');
    '''
               )


def downgrade() -> None:
    op.execute('''
    DELETE FROM users WHERE email = 'admin@admin.com' ''')
