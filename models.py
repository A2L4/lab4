from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Worker(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str]
    name: Mapped[str | None]
    username: Mapped[str]
    salary: Mapped[int]
    department_id: Mapped[int] = mapped_column(
        ForeignKey('departments.id'))

    department: Mapped['Department'] = relationship(
        back_populates='workers',
    )

    projects: Mapped[list['Project']] = relationship(
        back_populates='worker',
        cascade="all, delete-orphan",
    )


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    title: Mapped[str]
    worker_id: Mapped[int] = mapped_column(
        ForeignKey('workers.id'))

    worker: Mapped['Worker'] = relationship(
        back_populates='projects'
    )


class Department(Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    science_center_id: Mapped[int] = mapped_column(
        ForeignKey('science_centers.id'))

    workers: Mapped[list['Worker']] = relationship(
        back_populates='department',
        cascade="all, delete-orphan"
    )

    equipments: Mapped[list['Equipment']] = relationship(
        back_populates='department',
        cascade="all, delete-orphan"
    )

    science_center: Mapped['ScienceCenter'] = relationship(
        back_populates='departments'
    )


class Equipment(Base):
    __tablename__ = 'equipments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    state: Mapped[str]
    department_id: Mapped[int] = mapped_column(
        ForeignKey('departments.id'))

    department: Mapped['Department'] = relationship(
        back_populates='equipments',
    )


class ScienceCenter(Base):
    __tablename__ = 'science_centers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]

    departments: Mapped[list['Department']] = relationship(
        back_populates='science_center',
        cascade="all, delete-orphan"
    )
