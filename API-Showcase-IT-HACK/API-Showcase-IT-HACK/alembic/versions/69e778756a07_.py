"""empty message

Revision ID: 69e778756a07
Revises: 47f745bd236a
Create Date: 2024-09-13 03:18:08.955455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69e778756a07'
down_revision: Union[str, None] = '47f745bd236a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
