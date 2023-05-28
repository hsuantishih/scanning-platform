"""empty message

Revision ID: afea90fe6d7b
Revises: 78341f114aa1
Create Date: 2023-05-28 14:55:08.685233

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'afea90fe6d7b'
down_revision = '78341f114aa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=8),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=8),
               type_=mysql.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
