"""empty message

Revision ID: b1be7a797066
Revises: abcd061182b2
Create Date: 2025-04-10 01:40:16.316011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1be7a797066'
down_revision = 'abcd061182b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint('comment_author_id_fkey', type_='foreignkey')
        batch_op.drop_column('author_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('comment_author_id_fkey', 'user', ['author_id'], ['id'])

    # ### end Alembic commands ###
