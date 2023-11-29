"""empty message

Revision ID: 46220d4be995
Revises: 3e33d33ad464
Create Date: 2023-11-29 10:15:48.916616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46220d4be995'
down_revision = '3e33d33ad464'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hobby', schema=None) as batch_op:
        batch_op.alter_column('hobby1',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
        batch_op.alter_column('hobby2',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
        batch_op.alter_column('hobby3',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
        batch_op.alter_column('hobby4',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hobby', schema=None) as batch_op:
        batch_op.alter_column('hobby4',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
        batch_op.alter_column('hobby3',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
        batch_op.alter_column('hobby2',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
        batch_op.alter_column('hobby1',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)

    # ### end Alembic commands ###
