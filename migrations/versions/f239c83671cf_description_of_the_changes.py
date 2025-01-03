"""Description of the changes

Revision ID: f239c83671cf
Revises: 7d809cc4e8bb
Create Date: 2024-12-30 12:47:33.677391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f239c83671cf'
down_revision = '7d809cc4e8bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('location', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('transportation', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('size', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('product_id')
        batch_op.drop_column('user_id')
        batch_op.drop_column('total_price')
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('total_price', sa.FLOAT(), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('product_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'products', ['product_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('email')
        batch_op.drop_column('phone')
        batch_op.drop_column('size')
        batch_op.drop_column('transportation')
        batch_op.drop_column('location')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
