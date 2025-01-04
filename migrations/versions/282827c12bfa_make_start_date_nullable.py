"""Make start_date nullable

Revision ID: 282827c12bfa
Revises: 9e007009a607
Create Date: 2024-11-11 19:39:43.511312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '282827c12bfa'
down_revision = '9e007009a607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('is_approved', sa.Boolean(), nullable=True))
        batch_op.alter_column('start_date',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.alter_column('approved_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True)
        batch_op.alter_column('hours',
               existing_type=sa.TEXT(),
               type_=sa.String(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('hours',
               existing_type=sa.String(length=200),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('approved_at',
               existing_type=sa.DateTime(),
               type_=sa.TIMESTAMP(),
               existing_nullable=True)
        batch_op.alter_column('start_date',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.drop_column('is_approved')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
