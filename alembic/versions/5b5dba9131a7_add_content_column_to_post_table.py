"""add content column to post table

Revision ID: 5b5dba9131a7
Revises: f9b87c31e0ed
Create Date: 2023-07-18 14:32:34.491114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b5dba9131a7'
down_revision = 'f9b87c31e0ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
