
from fastapi import APIRouter
from app.models.student import Student, Student_Response
from app.services.student_service import add_student as add_student_service, get_all_students

student_router = APIRouter(
    prefix="/student"
)

#POSt requeste to add students details 
@student_router.post("/add", response_model=Student_Response)
async def add_student(student: Student):
    student_id = await add_student_service(student)
    return student


#i amm puuting in get requestt too gett all students details
@student_router.get("/", response_model=list[Student_Response])
async def getStudentDetails():
    return await get_all_students()