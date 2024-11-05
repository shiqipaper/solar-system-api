"""change columns

Revision ID: 206da339d6cf
Revises: 0de268c9f95d
Create Date: 2024-11-05 12:32:04.285615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '206da339d6cf'
down_revision = '0de268c9f95d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('random', sa.String(), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)
        batch_op.drop_column('distance_from_sun')
        batch_op.drop_column('surface_area')
        batch_op.drop_column('planet_id')
        batch_op.drop_column('moons_num')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('moons_num', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('planet_id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('surface_area', sa.NUMERIC(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('distance_from_sun', sa.NUMERIC(), autoincrement=False, nullable=True))
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('random')
        batch_op.drop_column('id')

    # ### end Alembic commands ###