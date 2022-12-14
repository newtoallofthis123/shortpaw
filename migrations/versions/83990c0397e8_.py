"""empty message

Revision ID: 83990c0397e8
Revises: 
Create Date: 2022-07-13 23:58:17.780588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83990c0397e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('og_url', sa.Text(), nullable=True),
    sa.Column('hash', sa.Text(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urls')
    # ### end Alembic commands ###
