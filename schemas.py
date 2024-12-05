from pydantic import BaseModel


class NewWorker(BaseModel):
    last_name: str
    name: str
    username: str | None
    salary: int
    department_id: int


class GetWorker(NewWorker):
    id: int
    department: 'GetDepartment'
    projects: list['GetProject']


class WorkerRel(GetWorker):          #
    department: 'GetDepartment'
    projects: list['GetProject']


class NewScienceCenter(BaseModel):
    name: str
    address: str


class GetScienceCenter(NewScienceCenter):
    id: int


class ScienceCenterRel(GetScienceCenter):    #
    departments: list['GetDepartment']


class NewDepartment(BaseModel):
    name: str
    science_center_id: int


class GetDepartment(NewDepartment):
    id: int


class DepartmentRel(GetDepartment):      #
    workers: list['GetWorker']
    equipments: list['GetEquipment']
    science_center: 'GetScienceCenter'


class NewEquipment(BaseModel):
    name: str
    state: str
    department_id: int


class GetEquipment(NewEquipment):
    id: int


class EquipmentRel(GetEquipment):
    department: 'GetDepartment'


class NewProject(BaseModel):
    name: str
    title: str
    worker_id: int


class GetProject(NewProject):
    id: int


class ProjectRel(GetProject):
    worker: 'GetWorker'
