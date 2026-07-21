#in this file there we are wrinting a business logic eg: to calclulate cgpa,% and all. 
#and all the logic , how the data is going to be manipulated/processed in background  #eg: is there any duplictae data

#inserting data in databse

from app.core.collections import student_collection
from app.models.student import Student

async def add_student(student: Student):
    result = await student_collection.insert_one(student.model_dump())
    return str(result.inserted_id)

async def get_all_students():
    cursor = student_collection.find()
    students = await cursor.to_list(length=100)
    return students


