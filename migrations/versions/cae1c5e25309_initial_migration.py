"""initial migration

Revision ID: cae1c5e25309
Revises: 
Create Date: 2024-12-04 13:15:31.707278

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cae1c5e25309'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('departments_science_center_id_fkey',
                       'departments', type_='foreignkey')
    op.create_foreign_key(None, 'departments', 'science_centers', [
                          'science_center_id'], ['id'])
    op.drop_constraint('equipments_department_id_fkey',
                       'equipments', type_='foreignkey')
    op.create_foreign_key(None, 'equipments', 'departments', [
                          'department_id'], ['id'])
    op.drop_constraint('projects_worker_id_fkey',
                       'projects', type_='foreignkey')
    op.create_foreign_key(None, 'projects', 'workers', ['worker_id'], ['id'])
    op.add_column('workers', sa.Column('username', sa.String(), nullable=True))
    op.alter_column('workers', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.drop_constraint('workers_department_id_fkey',
                       'workers', type_='foreignkey')
    op.create_foreign_key(None, 'workers', 'departments',
                          ['department_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workers', type_='foreignkey')
    op.create_foreign_key('workers_department_id_fkey', 'workers', 'departments', [
                          'department_id'], ['id'], ondelete='CASCADE')
    op.alter_column('workers', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.drop_column('workers', 'username')
    op.drop_constraint(None, 'projects', type_='foreignkey')
    op.create_foreign_key('projects_worker_id_fkey', 'projects', 'workers', [
                          'worker_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'equipments', type_='foreignkey')
    op.create_foreign_key('equipments_department_id_fkey', 'equipments', 'departments', [
                          'department_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'departments', type_='foreignkey')
    op.create_foreign_key('departments_science_center_id_fkey', 'departments', 'science_centers', [
                          'science_center_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###