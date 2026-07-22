#in this file there we are wrinting a business logic eg: to calclulate cgpa,% and all. 
#and all the logic , how the data is going to be manipulated/processed in background  #eg: is there any duplictae data

#inserting data in databse

from typing import Any, Optional
from app.core.collections import student_collection
from app.models.student import Student, Student_update, Student_Filter
from bson import ObjectId

async def add_student(student: Student):
    result = await student_collection.insert_one(student.model_dump())
    return str(result.inserted_id)

async def get_all_students():
    st = student_collection.find()
    students = await st.to_list(length=100)
    return students

async def getstudentbyid(id: str):

    result = await student_collection.find_one(
        {
            "_id": ObjectId(id)
        }
    )
    if result:
        #convert object_id into string
        result["_id"] = str(result["_id"])
    return result
#note:- we can also perform other database operations hereeg: update,delet,findone(by name,rollno,email,cgpa) etc

#update 
async def update_student(id, student):
    await student_collection.update_one(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": student.model_dump(exclude_unset=True)
        }
    )
    return student

#DELETE 
async def delete_student(id):
    await student_collection.delete_one(
        {
            "_id": ObjectId(id)
        }
    )
    return {"message": "Student deleted successfully"}


#filter student list
async def get_filtred_student_list(
    name: Optional[str] = None,
    rollno: Optional[int] = None,
    department: Optional[str] = None,
    min_cgpa: Optional[float] = None,
    max_cgpa: Optional[float] = None,
    email: Optional[str] = None,
):
    # build query according to the inputs 
    query: dict[str, Any] = {}

    #name
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    #rollno
    if rollno is not None:
        query["rollno"] = rollno
    #department
    if department:
        query["department"] = {"$regex": department, "$options": "i"}
    #cgpa
    if min_cgpa is not None or max_cgpa is not None:
        query["cgpa"] = {}
        if min_cgpa is not None:
            query["cgpa"]["$gte"] = min_cgpa
        if max_cgpa is not None:
            query["cgpa"]["$lte"] = max_cgpa
    #email
    if email:
        query["email"] = {"$regex": email, "$options": "i"}

    students = []
    async for student in student_collection.find(query):
        student["_id"] = str(student["_id"])
        students.append(student)
        
    return students

