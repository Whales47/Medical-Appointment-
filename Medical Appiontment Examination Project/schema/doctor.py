from enum import Enum
from typing import Optional
from pydantic import BaseModel


# Doctor Pydantic definition
class Doctors(BaseModel):
     id: int
     name: str
     specialization: str
     phone: str
     is_available: bool = True


# pydantic definition for Creating Doctor data
class DoctorsCreate(BaseModel):
     name: str
     specialization: str
     phone: str

     
# pydantic definition for Updating Doctor data
class DoctorsEdit(BaseModel):
     name: Optional[str] = None
     specialization: Optional[str] = None
     phone: Optional[str] = None
     

doctors: dict[int, Doctors] = {
     0: Doctors(id=0, name='Dr. Oke Faith', specialization='Dentist', phone='08097620243', is_available=False),
     1: Doctors(id=1, name='Dr. Alese Sherifat', specialization='Dermatologist', phone='08098725477'),
     2: Doctors(id=2, name='Dr. Ogunmosu Iyanuoluwa', specialization='Surgeon', phone='08088321883')

}