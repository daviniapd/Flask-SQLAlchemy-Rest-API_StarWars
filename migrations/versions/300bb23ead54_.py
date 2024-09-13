"""empty message

Revision ID: 300bb23ead54
Revises: bc069df15927
Create Date: 2024-09-13 21:50:33.296150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '300bb23ead54'
down_revision = 'bc069df15927'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite__character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('character_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('favorite__character_users_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite__character_characters_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'characters', ['character_id'], ['id'])
        batch_op.drop_column('characters_id')
        batch_op.drop_column('users_id')

    with op.batch_alter_table('favorite__planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('favorite__planet_planets_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite__planet_users_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planets', ['planet_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('users_id')
        batch_op.drop_column('planets_id')

    with op.batch_alter_table('favorite__vehicle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('vehicle_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('favorite__vehicle_users_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite__vehicle_vehicles_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'vehicles', ['vehicle_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('vehicles_id')
        batch_op.drop_column('users_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite__vehicle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('vehicles_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorite__vehicle_vehicles_id_fkey', 'vehicles', ['vehicles_id'], ['id'])
        batch_op.create_foreign_key('favorite__vehicle_users_id_fkey', 'users', ['users_id'], ['id'])
        batch_op.drop_column('vehicle_id')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('favorite__planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planets_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorite__planet_users_id_fkey', 'users', ['users_id'], ['id'])
        batch_op.create_foreign_key('favorite__planet_planets_id_fkey', 'planets', ['planets_id'], ['id'])
        batch_op.drop_column('planet_id')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('favorite__character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('characters_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorite__character_characters_id_fkey', 'characters', ['characters_id'], ['id'])
        batch_op.create_foreign_key('favorite__character_users_id_fkey', 'users', ['users_id'], ['id'])
        batch_op.drop_column('character_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###