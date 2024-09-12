"""empty message

Revision ID: 214a4aa2033d
Revises: 5c0357692816
Create Date: 2024-09-12 11:27:15.350195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '214a4aa2033d'
down_revision = '5c0357692816'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('galactic_location', sa.String(length=120), nullable=True),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.Column('population', sa.String(length=120), nullable=True),
    sa.Column('native_species', sa.String(length=120), nullable=True),
    sa.Column('government', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('galactic_location'),
    sa.UniqueConstraint('government'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('native_species'),
    sa.UniqueConstraint('population')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
