"""Initial Migration

Revision ID: 151dd2c2d79e
Revises: 7112a1a905e7
Create Date: 2019-09-12 08:33:24.214069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '151dd2c2d79e'
down_revision = '7112a1a905e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
