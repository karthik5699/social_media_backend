"""create posts table

Revision ID: f9b87c31e0ed
Revises: 
Create Date: 2023-07-18 14:20:42.106700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9b87c31e0ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
