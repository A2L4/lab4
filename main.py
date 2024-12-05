from fastapi import FastAPI
import uvicorn
from orm import SyncOrm
from schemas import NewWorker, NewScienceCenter, NewDepartment, NewEquipment, NewProject

app = FastAPI()


@app.post(
    '/science_centers',
    tags=['Научные организации'],
    summary='Создать научную организацию'
)
def create_science_center(new_science_center: NewScienceCenter):
    SyncOrm.create_science_center(
        new_science_center.name, new_science_center.address)
    return {'OK': True}


@app.get(
    '/science_centers',
    tags=['Научные организации'],
    summary='Список всех организаций'
)
def get_science_centers():
    science_centers = SyncOrm.get_science_centers()
    return science_centers


@app.put(
    '/science_centers',
    tags=['Научные организации'],
    summary='Изменить адрес организации'
)
def change_science_center_address(science_center_id: int, new_address: str):
    SyncOrm.update_science_center_address(science_center_id, new_address)
    return {'OK': True}


@app.delete(
    '/science_centers',
    tags=['Научные организации'],
    summary='Удалить организацию'
)
def delete_science_center(science_center_id: int):
    SyncOrm.delete_science_center(science_center_id)
    return {'OK': True}


@app.post(
    '/departments',
    tags=['Отделы'],
    summary='Создать отдел'
)
def create_department(new_department: NewDepartment):
    SyncOrm.create_department(
        new_department.name, new_department.science_center_id)
    return {'OK': True}


@app.get(
    '/departments',
    tags=['Отделы'],
    summary='Список отделов'
)
def get_departments():
    departments = SyncOrm.get_departments()
    return departments


@app.put(
    '/departments',
    tags=['Отделы'],
    summary='Изменить название отдела'
)
def change_department_name(department_id: int, new_name: str):
    SyncOrm.update_department_name(department_id, new_name)
    return {'OK': True}


@app.delete(
    '/departments',
    tags=['Отделы'],
    summary='Удалить отдел'
)
def delete_department(department_id: int):
    SyncOrm.delete_department(department_id)
    return {'OK': True}


@app.post(
    '/workers',
    tags=['Сотрудники'],
    summary='Создать сотрудника'
)
def create_worker_(new_worker: NewWorker):
    SyncOrm.create_worker(new_worker.last_name, new_worker.name,
                          new_worker.username, new_worker.salary, new_worker.department_id)
    return {'OK': True}


@app.get(
    '/workers',
    tags=['Сотрудники'],
    summary='Список всех сотрудников'
)
def get_workers():
    workers = SyncOrm.get_workers()
    return workers


@app.put(
    '/workers',
    tags=['Сотрудники'],
    summary='Изменить зарплату'
)
def change_salary(worker_id: int, new_salary: int):
    SyncOrm.update_worker_salary(worker_id, new_salary)
    return {'OK': True}


@app.delete(
    '/workers',
    tags=['Сотрудники'],
    summary='Удалить сотрудника'
)
def delete_worker(worker_id: int):
    SyncOrm.delete_worker(worker_id)
    return {'OK': True}


@app.post(
    '/equipments',
    tags=['Оборудование'],
    summary='Создать оборудование'
)
def create_equipment(new_equipment: NewEquipment):
    SyncOrm.create_equipment(
        new_equipment.name, new_equipment.state, new_equipment.department_id)
    return {'OK': True}


@app.get(
    '/equipments',
    tags=['Оборудование'],
    summary='Список оборудования'
)
def get_equipments():
    equipments = SyncOrm.get_equipments()
    return equipments


@app.put(
    '/equipments',
    tags=['Оборудование'],
    summary='Изменить состояние оборудования'
)
def change_equipment_state(equipment_id: int, new_state: str):
    SyncOrm.update_equipment_state(equipment_id, new_state)
    return {'OK': True}


@app.delete(
    '/equipments',
    tags=['Оборудование'],
    summary='Удалить оборудование'
)
def delete_equipment(equipment_id: int):
    SyncOrm.delete_equipment(equipment_id)
    return {'OK': True}


@app.post(
    '/projects',
    tags=['Проекты'],
    summary='Создать проект'
)
def create_project(new_project: NewProject):
    SyncOrm.create_project(
        new_project.name, new_project.title, new_project.worker_id)
    return {'OK': True}


@app.get(
    '/projects',
    tags=['Проекты'],
    summary='Список проектов'
)
def get_projects():
    projects = SyncOrm.get_projects()
    return projects


@app.put(
    '/projects',
    tags=['Проекты'],
    summary='Изменить описание проекта'
)
def change_project_title(project_id: int, new_title: str):
    SyncOrm.update_project_title(project_id, new_title)
    return {'OK': True}


@app.delete(
    '/projects',
    tags=['Проекты'],
    summary='Удалить проект'
)
def delete_project(project_id: int):
    SyncOrm.delete_project(project_id)
    return {'OK': True}


if __name__ == '__main__':

    SyncOrm.create_tables()
    uvicorn.run('main:app', reload=True)
