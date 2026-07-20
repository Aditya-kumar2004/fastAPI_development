from fastapi import FastAPI 

app = FastAPI()

#this alll are synchrounous API
@app.get("/")
def read_root():
	return {"message": "Welcome to the fastAPI development!"}

	
@app.get("/home")
def home():
	return {"message": "Welcome to the HOME page!"}

@app.get("/about")
def about():
	return {"message": "Welcome to the ABOUT page!"}

#this alll are Asynchrounous API
@app.get("/contact")
async def contact():
	return {"message": "Welcome to the CONTACT pAGE!"}

@app.get("/dasboard")
async def dasboard():
	return {"message": "Welcome to the  DASBOARD!"}

@app.get("/getdata")
async def get_data():
	students = [
		{"id": 1, "name": "Aisha Khan", "age": 21, "email": "aisha.khan@example.com", "score": 88.5},
		{"id": 2, "name": "Carlos Mendes", "age": 24, "email": "carlos.mendes@example.com", "score": 92.0},
		{"id": 3, "name": "Lina Petrova", "age": 19, "email": "lina.petrova@example.com", "score": 76.0},
		{"id": 4, "name": "Rahul Sharma", "age": 22, "email": "rahul.sharma@example.com", "score": 81.25},
		{"id": 5, "name": "Maya Thompson", "age": 20, "email": "maya.thompson@example.com", "score": 69.5},
	]
	return students

#pasing parameters in url

@app.get("/getdata1/{id:int}")
def path_param(id):
	return f"Students id: {id}"

#task1:- create s students list with name
#		if entered name is in list/data simply retun it
#		otherwise retrun messgae data not found


#query parameters: to get filtered or sorted result
#?department = CSE&cgpa = 5.5

@app.get("/students")
def get_query(name:str,depart:str,cgpa:float):

	students2 = [
		{"name": "Aditya", "rollno": 5, "depart": "CSE", "CGPA": 5.5},
		{"name": "Priya", "rollno": 6, "depart": "CSE", "CGPA": 6.0},
		{"name": "Vikram", "rollno": 7, "depart": "ECE", "CGPA": 7.2},
		{"name": "Sonia", "rollno": 8, "depart": "ME", "CGPA": 6.8},
		{"name": "Rohit", "rollno": 9, "depart": "CSE", "CGPA": 5.9},
		{"name": "Neha", "rollno": 10, "depart": "IT", "CGPA": 6.5},
	]

	# acc to query parameters: filter by department (exact, case-insensitive),
	# name (substring, case-insensitive), and CGPA (>= given value)
	result = []
	for s in students2:
		if s.get("depart", "").lower() == depart.lower() and s.get("CGPA", 0) >= cgpa and name.lower() in s.get("name", "").lower():
			result.append(s)

	return result


#pydantic

from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    rollno: int
    department: str
    cgpa: float = Field(..., gt=4)
    email: EmailStr

students = []

@app.post("/student/add")
def student_model(student: Student):

    students.append(student)
    return {"message": "Student Added :", "student": student, "all_students": students}


#Field : apply explicit valid
#name: must be greater than 3 char max 50
#age : 