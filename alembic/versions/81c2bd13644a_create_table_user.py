"""create table user

Revision ID: 81c2bd13644a
Revises:
Create Date: 2022-11-24 13:00:46.846834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81c2bd13644a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    '''
    class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    password = Column(String(200))
    email = Column(String(150), unique=True)
    national_id = Column(String(20))

    file_path = Column(String(100))
    phone_number = Column(String(20))
    loans = relationship("Loan", back_populates="customer",
                         cascade="all, delete")
    roles = relationship("Roles", back_populates="customer")
'''
    op.execute('''
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        password VARCHAR(200) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        national_id VARCHAR(20) NOT NULL,
        file_path VARCHAR(100) ,
        phone_number VARCHAR(20) NOT NULL
    );
    ''')


def downgrade() -> None:
    op.execute('''
    DROP TABLE users;
    ''')
