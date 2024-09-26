"""private

Revision ID: 408caba3b387
Revises: e4668cc4351a
Create Date: 2024-09-12 18:26:43.767851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '408caba3b387'
down_revision: Union[str, None] = 'e4668cc4351a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
