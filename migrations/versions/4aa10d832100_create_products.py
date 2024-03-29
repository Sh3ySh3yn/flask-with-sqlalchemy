"""create products

Revision ID: 4aa10d832100
Revises: 
Create Date: 2019-04-04 15:42:38.830532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aa10d832100'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
