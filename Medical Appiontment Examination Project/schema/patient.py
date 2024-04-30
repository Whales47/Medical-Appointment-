from typing import Optional
from pydantic import BaseModel


# patient pydantic definition
class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


# pydantic definition Creating patient data
class PatientsCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


# pydantic definition for updating patient data
class PatientsEdit(BaseModel):
    name: Optional[str]=None
    age: Optional[int] = None
    sex: Optional[str] = None
    weight: Optional[float]=None
    height: Optional[float]=None
    phone: Optional[str] = None
    

patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='Ilyas Abubakar', age=28, sex= 'male', weight=85.5, height=182.8, phone= '08128695353'
	),
    1: Patients(
        id=1, name='Olusola Olanrewaju', age=25, sex= 'female', weight=89.0, height=152.4, phone= '09077867238'
	),
    2: Patients(
        id=2, name='Segun Ayeni', age=30, sex= 'male', weight=83.5, height=160.0, phone= '08132482853'
	)
}