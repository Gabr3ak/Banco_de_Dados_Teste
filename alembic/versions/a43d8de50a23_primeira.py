"""primeira

Revision ID: a43d8de50a23
Revises:
Create Date: 2024-06-26 17:55:10.342224

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a43d8de50a23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'livros',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('titulo', sa.String(length=50), nullable=False),
        sa.Column('autor', sa.String(length=50), nullable=False),
        sa.Column('isbn', sa.String(length=13), unique=True, nullable=False),
        sa.Column('data_publicacao', sa.Date),
        sa.Column('disponivel', sa.Boolean, default=True)
    )
    op.create_table(
        'membros',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), unique=True, nullable=False),
        sa.Column('data_entrada', sa.Date, nullable=False)
    )
    op.create_table(
        'emprestimos',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('id_livro', sa.Integer(), sa.ForeignKey('livros.id'), nullable=False),
        sa.Column('id_membro', sa.Integer(), sa.ForeignKey('membros.id'), nullable=False),
        sa.Column('data_emprestimo', sa.Date, nullable=False),
        sa.Column('data_entrega', sa.Date)
    )


def downgrade() -> None:
    op.drop_table('emprestimos')
    op.drop_table('membros')
    op.drop_table('livros')

