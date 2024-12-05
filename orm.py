from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import Department, Equipment, Project, Worker, ScienceCenter
from database import engine, Base, session_factory
from schemas import DepartmentRel, EquipmentRel, ProjectRel, ScienceCenterRel, WorkerRel


class SyncOrm():

    @staticmethod
    def create_tables():
        engine.echo = True
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = True

    @staticmethod
    def create_worker(worker_last_name, worker_name, worker_username, worker_salary, worker_department_id):
        with session_factory() as session:
            worker = Worker(last_name=worker_last_name, name=worker_name, username=worker_username,
                            salary=worker_salary, department_id=worker_department_id)
            session.add(worker)
            session.commit()

    @staticmethod
    def get_workers():
        with session_factory() as session:
            query = (
                select(Worker)
                .options(selectinload(Worker.projects))
            )
            res = session.execute(query)
            result_orm = res.scalars().all()
            result_dto = [WorkerRel.model_validate(
                row, from_attributes=True) for row in result_orm]
            return result_dto

    @staticmethod
    def update_worker_salary(worker_id, new_salary):
        with session_factory() as session:
            worker = session.get(Worker, worker_id)
            worker.salary = new_salary
            session.commit()

    @staticmethod
    def delete_worker(worker_id):
        with session_factory() as session:
            worker = session.get(Worker, worker_id)
            if worker:
                session.delete(worker)
                session.commit()

    @staticmethod
    def create_science_center(science_center_name, science_center_address):
        with session_factory() as session:
            science_center = ScienceCenter(
                name=science_center_name, address=science_center_address)
            session.add(science_center)
            session.commit()

    @staticmethod
    def get_science_centers():
        with session_factory() as session:
            query = (
                select(ScienceCenter)
                .options(selectinload(ScienceCenter.departments))
            )
            res = session.execute(query)
            result_orm = res.scalars().all()
            result_dto = [ScienceCenterRel.model_validate(
                row, from_attributes=True) for row in result_orm]
            return result_dto

    @staticmethod
    def update_science_center_address(science_center_id, new_address):
        with session_factory() as session:
            science_center = session.get(ScienceCenter, science_center_id)
            science_center.address = new_address
            session.commit()

    @staticmethod
    def delete_science_center(science_center_id):
        with session_factory() as session:
            science_center = session.get(ScienceCenter, science_center_id)
            if science_center:
                session.delete(science_center)
                session.commit()

    @staticmethod
    def create_department(department_name, science_center_id_):
        with session_factory() as session:
            department = Department(
                name=department_name, science_center_id=science_center_id_)
            session.add(department)
            session.commit()

    @staticmethod
    def get_departments():
        with session_factory() as session:
            query = (
                select(Department)
                .options(selectinload(Department.workers))
                .limit(2)
            )
            res = session.execute(query)
            result_orm = res.scalars().all()
            result_dto = [DepartmentRel.model_validate(
                row, from_attributes=True) for row in result_orm]
            return result_dto

    @staticmethod
    def update_department_name(department_id, new_name):
        with session_factory() as session:
            department = session.get(Department, department_id)
            department.name = new_name
            session.commit()

    @staticmethod
    def delete_department(department_id):
        with session_factory() as session:
            department = session.get(Department, department_id)
            if department:
                session.delete(department)
                session.commit()

    @staticmethod
    def create_equipment(equipment_name, equipment_state, department_id_):
        with session_factory() as session:
            equipment = Equipment(
                name=equipment_name, state=equipment_state, department_id=department_id_)
            session.add(equipment)
            session.commit()

    @staticmethod
    def get_equipments():
        with session_factory() as session:
            query = (
                select(Equipment)
                .options(selectinload(Equipment.department))
            )
            res = session.execute(query)
            result_orm = res.scalars().all()
            result_dto = [EquipmentRel.model_validate(
                row, from_attributes=True) for row in result_orm]
            return result_dto

    @staticmethod
    def update_equipment_state(equipment_id, new_state):
        with session_factory() as session:
            equipment = session.get(Equipment, equipment_id)
            equipment.state = new_state
            session.commit()

    @staticmethod
    def delete_equipment(equipment_id):
        with session_factory() as session:
            equipment = session.get(Equipment, equipment_id)
            if equipment:
                session.delete(equipment)
                session.commit()

    @staticmethod
    def create_project(project_name, project_title, worker_id_):
        with session_factory() as session:
            project = Project(
                name=project_name, title=project_title, worker_id=worker_id_)
            session.add(project)
            session.commit()

    @staticmethod
    def get_projects():
        with session_factory() as session:
            query = (
                select(Project)
                .options(selectinload(Project.worker))
            )
            res = session.execute(query)
            result_orm = res.scalars().all()
            result_dto = [ProjectRel.model_validate(
                row, from_attributes=True) for row in result_orm]
            return result_dto

    @staticmethod
    def update_project_title(project_id, new_title):
        with session_factory() as session:
            project = session.get(Project, project_id)
            project.title = new_title
            session.commit()

    @staticmethod
    def delete_project(project_id):
        with session_factory() as session:
            project = session.get(Project, project_id)
            if project:
                session.delete(project)
                session.commit()
