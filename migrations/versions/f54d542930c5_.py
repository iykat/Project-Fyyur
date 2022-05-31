"""empty message

Revision ID: f54d542930c5
Revises: df20c3dccd24
Create Date: 2022-05-31 09:02:38.313455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f54d542930c5'
down_revision = 'df20c3dccd24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.drop_column('Artist', 'venue')
    op.drop_column('Artist', 'description')
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=800), nullable=True))
    op.drop_column('Venue', 'talent')
    op.drop_column('Venue', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('description', sa.VARCHAR(length=800), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.add_column('Artist', sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('venue', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
