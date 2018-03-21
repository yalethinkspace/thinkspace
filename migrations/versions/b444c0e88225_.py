"""empty message

Revision ID: b444c0e88225
Revises: c3e1b5a705f3
Create Date: 2018-03-21 00:39:24.932637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b444c0e88225'
down_revision = 'c3e1b5a705f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'subtitle',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'subtitle',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###