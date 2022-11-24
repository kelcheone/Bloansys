"""create table guarantors

Revision ID: 2fc8e53082b6
Revises: 32e9fccdd773
Create Date: 2022-11-24 13:28:35.894172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fc8e53082b6'
down_revision = '32e9fccdd773'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
    CREATE TABLE guarantors (
        guarantor_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        national_id VARCHAR(20) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        email VARCHAR(150) NOT NULL,
        file_path VARCHAR(100),
        loan_id INTEGER NOT NULL,
        FOREIGN KEY (loan_id) REFERENCES loans(loan_id) ON DELETE CASCADE
    );
    ''')


def downgrade() -> None:
    op.execute('''
    DROP TABLE guarantors CASCADE;
    ''')
