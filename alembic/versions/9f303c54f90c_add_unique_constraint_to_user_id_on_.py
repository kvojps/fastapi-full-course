"""add_unique_constraint_to_user_id_on_account_table

Revision ID: 9f303c54f90c
Revises: ee65ed246057
Create Date: 2024-08-04 11:05:43.472865

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f303c54f90c'
down_revision: Union[str, None] = 'ee65ed246057'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'accounts', ['user_id'])
    op.drop_constraint('accounts_user_id_fkey', 'accounts', type_='foreignkey')
    op.create_foreign_key(None, 'accounts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'accounts', type_='foreignkey')
    op.create_foreign_key('accounts_user_id_fkey', 'accounts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'accounts', type_='unique')
    # ### end Alembic commands ###
