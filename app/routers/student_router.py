
from fastapi import Query
from fastapi import APIRouter
from app.models.student import Student, Student_Response, Student_update
#servicee i will importt here
from app.services.student_service import (
    add_student as add_student_service,
    get_all_students,
    getstudentbyid as get_student_by_id_service,
    update_student,
    delete_student,
    get_filtred_student_list
)

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


@student_router.get("/getbyid/{id}")
async def getstudentbyid(id: str):
    return await get_student_by_id_service(id)


#get student by id
@student_router.get("/getone", response_model=Student_Response)
async def getoneStudent(id: str):
    return await get_student_by_id_service(id)


#update 
@student_router.put("/update", response_model=Student_update)
async def updateStudent(id, student: Student_update):
    return await update_student(id, student)

#delete
@student_router.delete("/delete")
async def deleteStudent(id):
    await delete_student(id)
    return f"student deleted successfully"

#filter
@student_router.get("/filter")
async def get_filtered_students(
    name:str = Query(None, description="filter by name"),
    rollno:int = Query(None, description="filter by rollno"),
    department:str = Query(None, description="filter by department"),
    min_cgpa:float = Query(None, description="filter by min_cgpa"),
    max_cgpa:float = Query(None, description="filter by max_cgpa"),
    email:str = Query(None, description="filter by email")
):
    if any([name, rollno, department, min_cgpa, max_cgpa, email]):
        return await get_filtred_student_list(
            name = name,
            rollno = rollno,
            department = department,
            min_cgpa = min_cgpa,
            max_cgpa = max_cgpa,
            email = email
        )
    else:
        return await get_all_students()



