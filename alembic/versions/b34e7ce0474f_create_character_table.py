"""create character table

Revision ID: b34e7ce0474f
Revises: 
Create Date: 2023-07-05 17:42:42.533489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b34e7ce0474f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('character',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('character', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('character')
