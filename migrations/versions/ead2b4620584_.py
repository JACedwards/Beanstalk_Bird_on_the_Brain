"""empty message

Revision ID: ead2b4620584
Revises: 9ccea57d8c9e
Create Date: 2022-05-30 09:51:15.244034

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ead2b4620584'
down_revision = '9ccea57d8c9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bird', sa.Column('common_name', sa.String(length=100), nullable=False))
    op.add_column('bird', sa.Column('species', sa.String(length=100), nullable=True))
    op.add_column('bird', sa.Column('city', sa.String(length=60), nullable=True))
    op.add_column('bird', sa.Column('county', sa.String(length=50), nullable=False))
    op.add_column('bird', sa.Column('state', sa.String(length=30), nullable=False))
    op.add_column('bird', sa.Column('date', sa.DateTime(), nullable=False))
    op.add_column('bird', sa.Column('comments', sa.String(length=500), nullable=True))
    op.add_column('bird', sa.Column('image', sa.String(length=500), nullable=True))
    op.add_column('bird', sa.Column('diet', sa.String(length=75), nullable=True))
    op.add_column('bird', sa.Column('price', sa.Float(precision=2), nullable=True))
    op.add_column('bird', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.drop_column('bird', 'latin_name')
    op.drop_column('bird', 'created')
    op.drop_column('bird', 'food')
    op.drop_column('bird', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bird', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('bird', sa.Column('food', sa.VARCHAR(length=75), autoincrement=False, nullable=True))
    op.add_column('bird', sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('bird', sa.Column('latin_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('bird', 'created_on')
    op.drop_column('bird', 'price')
    op.drop_column('bird', 'diet')
    op.drop_column('bird', 'image')
    op.drop_column('bird', 'comments')
    op.drop_column('bird', 'date')
    op.drop_column('bird', 'state')
    op.drop_column('bird', 'county')
    op.drop_column('bird', 'city')
    op.drop_column('bird', 'species')
    op.drop_column('bird', 'common_name')
    # ### end Alembic commands ###
