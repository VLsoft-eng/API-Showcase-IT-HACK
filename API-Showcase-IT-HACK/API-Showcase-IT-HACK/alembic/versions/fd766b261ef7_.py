"""empty message

Revision ID: fd766b261ef7
Revises: 69e778756a07
Create Date: 2024-09-13 03:26:15.952911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd766b261ef7'
down_revision: Union[str, None] = '69e778756a07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
