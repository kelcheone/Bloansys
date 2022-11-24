"""create table transactions

Revision ID: bbf2815b8774
Revises: 2fc8e53082b6
Create Date: 2022-11-24 13:31:12.604429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbf2815b8774'
down_revision = '2fc8e53082b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
    CREATE TABLE transactions (
        transaction_id SERIAL PRIMARY KEY,
        amount NUMERIC(10, 2) NOT NULL,
        transaction_type VARCHAR(50) NOT NULL,
        transaction_date VARCHAR(50) NOT NULL,
        loan_id INTEGER NOT NULL,
        FOREIGN KEY (loan_id) REFERENCES loans(loan_id) ON DELETE CASCADE
        
    );
    ''')


def downgrade() -> None:
    op.execute('''
    DROP TABLE transactions CASCADE;
    ''')
