"""empty message

Revision ID: 6302f94568be
Revises: a36cb7a1f46d
Create Date: 2023-12-01 17:23:53.595404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6302f94568be'
down_revision = 'a36cb7a1f46d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hobby', schema=None) as batch_op:
        batch_op.alter_column('filename',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hobby', schema=None) as batch_op:
        batch_op.alter_column('filename',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)

    # ### end Alembic commands ###
