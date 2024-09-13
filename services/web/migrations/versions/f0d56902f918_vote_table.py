"""vote table

Revision ID: f0d56902f918
Revises: 834b1a697901
Create Date: 2024-08-25 01:49:26.018578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0d56902f918'
down_revision = '834b1a697901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('suggested_name', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_vote_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_vote_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_vote_user_id'))
        batch_op.drop_index(batch_op.f('ix_vote_timestamp'))

    op.drop_table('vote')
    # ### end Alembic commands ###
