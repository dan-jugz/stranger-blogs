"""other Migration

Revision ID: 041a6fbfe786
Revises: 802afdbad763
Create Date: 2019-08-13 10:02:33.827438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041a6fbfe786'
down_revision = '802afdbad763'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('writer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'writers', ['writer_id'], ['id'])
    op.add_column('subscribers', sa.Column('writer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subscribers', 'writers', ['writer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subscribers', type_='foreignkey')
    op.drop_column('subscribers', 'writer_id')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'writer_id')
    # ### end Alembic commands ###
