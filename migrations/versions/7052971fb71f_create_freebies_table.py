"""create freebies table

Revision ID: 7052971fb71f
Revises: 
Create Date: 2025-06-02 16:38:34.001433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7052971fb71f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("freebies",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("item_name", sa.String()),
        sa.Column("value", sa.Integer()),
        sa.Column("dev_id", sa.Integer(), sa.ForeignKey("devs.id")),
        sa.Column("company_id", sa.Integer(), sa.ForeignKey("companies.id")),
    )


def downgrade():
    op.drop_table("freebies")
