
from fastapi import APIRouter
from app.models.student import Student, Student_Response

student_router = APIRouter(
    prefix="/student"
)

#this i have created list where store all student details
students = []
#POSt requeste to add students details 
@student_router.post("/add", response_model=Student_Response)
def add_student(student: Student):

    students.append(student)

    return student

#i amm puuting in get requestt too gett all students details
@student_router.get("/", response_model=list[Student_Response])
def getStudentDetails():
	return students