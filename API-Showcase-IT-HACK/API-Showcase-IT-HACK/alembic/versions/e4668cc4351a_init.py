"""init

Revision ID: e4668cc4351a
Revises: 3954e2eec39f
Create Date: 2024-09-12 12:54:51.848700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4668cc4351a'
down_revision: Union[str, None] = '3954e2eec39f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
