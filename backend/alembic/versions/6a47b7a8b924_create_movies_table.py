"""create movies table

Revision ID: 6a47b7a8b924
Revises:
Create Date: 2025-11-14 14:58:11.426235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a47b7a8b924'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('folder', sa.String(200), nullable=False),
        sa.Column('year', sa.String(4), nullable=False),
        sa.Column('country', sa.String(100), nullable=True),
        sa.Column('director', sa.String(50), nullable=True),
        sa.Column('type', sa.String(80), nullable=True),
        sa.Column('comment', sa.Unicode(4000)),
    )


def downgrade() -> None:
    op.drop_table('movies')
