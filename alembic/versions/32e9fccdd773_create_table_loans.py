"""create table loans

Revision ID: 32e9fccdd773
Revises: 81c2bd13644a
Create Date: 2022-11-24 13:24:42.678983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32e9fccdd773'
down_revision = '81c2bd13644a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # user_id = Column(Integer, ForeignKey("users.user_id"))
    op.execute('''
    CREATE TABLE loans (
        loan_id SERIAL PRIMARY KEY,
        amount NUMERIC(10, 2) NOT NULL,
        interest NUMERIC(10, 2) NOT NULL,
        balance NUMERIC(10, 2) NOT NULL,
        due_date VARCHAR(50) NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    );
    ''')


def downgrade() -> None:
    op.execute('''
    DROP TABLE loans CASCADE;
    ''')
