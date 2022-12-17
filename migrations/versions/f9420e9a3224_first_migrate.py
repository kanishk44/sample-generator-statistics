"""First migrate

Revision ID: f9420e9a3224
Revises: 
Create Date: 2022-12-17 13:08:11.189814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9420e9a3224'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sample_calc', schema=None) as batch_op:
        batch_op.drop_column('z_score')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sample_calc', schema=None) as batch_op:
        batch_op.add_column(sa.Column('z_score', sa.NUMERIC(precision=10, scale=2), nullable=True))

    # ### end Alembic commands ###