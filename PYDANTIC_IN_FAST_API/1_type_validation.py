
from pydantic import BaseModel
from typing import List , Dict , Optional

class patient(BaseModel):
    name : str
    age : int
    weight: float
    married : bool
    allergies :Optional[List[str]] = None
    contact_details = Dict[str,str]

def inser_patient_data(patient :patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient :patient):
    print(patient.name)
    print(patient.age) 
    print('updated')

patient_info = {'name':'dipali', 'age':22, 'weight':40.1, 'married':True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'dipali7@gmail.com','phone':'1234567890'}}           

patien1 = patient(**patient_info)

update_patient_data(patien1)