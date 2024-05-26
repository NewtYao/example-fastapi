"""add content column to posts table

Revision ID: 4736c3cc7ec7
Revises: 15a4a0df98e1
Create Date: 2024-05-25 14:34:13.632343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4736c3cc7ec7'
down_revision: Union[str, None] = '15a4a0df98e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
