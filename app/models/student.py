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
