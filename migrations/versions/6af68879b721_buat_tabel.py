"""buat tabel

Revision ID: 6af68879b721
Revises: 8193333789cf
Create Date: 2024-04-12 17:30:11.290920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6af68879b721'
down_revision = '8193333789cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('komitmen',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.DateTime(), nullable=False),
    sa.Column('jumlah_barang', sa.Integer(), nullable=False),
    sa.Column('satuan', sa.String(length=10), nullable=False),
    sa.Column('status', sa.Enum('PROSES', 'COMPLETE', 'FAILED', name='status'), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('id_material', sa.BigInteger(), nullable=True),
    sa.Column('id_pekerjaan', sa.BigInteger(), nullable=True),
    sa.Column('id_officer', sa.BigInteger(), nullable=True),
    sa.Column('id_user', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id_material'], ['material.id'], ),
    sa.ForeignKeyConstraint(['id_officer'], ['officer.id'], ),
    sa.ForeignKeyConstraint(['id_pekerjaan'], ['pekerjaan.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pengguna',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('no_identitas', sa.String(length=25), nullable=False),
    sa.Column('no_hp', sa.String(length=20), nullable=False),
    sa.Column('id_unit', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id_unit'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('no_hp')
    )
    op.create_table('picking',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.DateTime(), nullable=False),
    sa.Column('no_reservasi', sa.String(length=10), nullable=False),
    sa.Column('jumlah_barang', sa.Integer(), nullable=False),
    sa.Column('satuan', sa.String(length=10), nullable=False),
    sa.Column('status', sa.Enum('PROSES', 'COMPLETE', 'FAILED', name='status'), nullable=False),
    sa.Column('id_material', sa.BigInteger(), nullable=True),
    sa.Column('id_pekerjaan', sa.BigInteger(), nullable=True),
    sa.Column('id_officer', sa.BigInteger(), nullable=True),
    sa.Column('id_user', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id_material'], ['material.id'], ),
    sa.ForeignKeyConstraint(['id_officer'], ['officer.id'], ),
    sa.ForeignKeyConstraint(['id_pekerjaan'], ['pekerjaan.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('no_reservasi')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('picking')
    op.drop_table('pengguna')
    op.drop_table('komitmen')
    # ### end Alembic commands ###
