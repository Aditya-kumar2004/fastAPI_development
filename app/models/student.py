from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    rollno: int
    department: str
    cgpa: float = Field(..., gt=4)
    email: EmailStr
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")     #r:-regex=TO froma specific patterns
    aadhar: str = Field(..., pattern=r"^\d{12}$")
    pancard: str = Field(..., pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    password: str = Field(..., min_length=8)

class Student_Response(BaseModel):
    name: str
    rollno: int
    department: str
    email: str


class Student_update(BaseModel):
    name:Optional[str] = None
    rollno:Optional[int] = None
    department:Optional[str] = None
    cgpa:Optional[float] = None
    email:Optional[EmailStr] = None
    phone:Optional[str] = None
    aadhar:Optional[str] = None
    pancard:Optional[str] = None
    password:Optional[str] = None


class Student_Filter(BaseModel):
    name:Optional[str] = None
    rollno:Optional[int] = None
    department:Optional[str] = None
    min_cgpa:Optional[float] = None
    max_cgpa:Optional[float] = None
    email:Optional[EmailStr] = None
