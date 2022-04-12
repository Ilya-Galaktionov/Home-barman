"""added email to user

Revision ID: 99304b834c87
Revises: 
Create Date: 2022-04-12 22:26:40.529041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99304b834c87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cocktails', ['id'])
    op.create_unique_constraint(None, 'raiting', ['id'])
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'email')
    op.drop_constraint(None, 'raiting', type_='unique')
    op.drop_constraint(None, 'cocktails', type_='unique')
    # ### end Alembic commands ###
