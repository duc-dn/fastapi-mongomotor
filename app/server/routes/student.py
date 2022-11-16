from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import AsyncMongoConnect
from app.server.models.student import ResponseModel, StudentSchema, ErrorResponseModel

router = APIRouter()

@router.post("/add", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    mg = AsyncMongoConnect("students")
    # use JSON Compatible Encoder from FastAPI to convert our models into a format JSON
    student = jsonable_encoder(student)
    doc_id = await mg.add_student("students_collection", student)
    return ResponseModel(doc_id, "Student added sucessfully")


@router.get("/", response_description="students retrieved")
async def get_students():
    mg = AsyncMongoConnect("students")
    students = await mg.retrieve_students("students_collection")
    print(students)
    if students:
        return ResponseModel(students, "Students data retrieved sucessfully")
    return ResponseModel(students, "Empty list returned")

@router.get("/{id}", response_description="student data retrieved")
async def get_student_data(id):
    mg = AsyncMongoConnect("students")
    student = await mg.retrieve_student("students_collection", id)
    if student:
        return ResponseModel(student, "Student data retrieved sucessfully")
    return ErrorResponseModel("An error occurred", 404, "Student doesn't exist")

@router.delete("{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    mg = AsyncMongoConnect("students")
    deleted_student = await mg.delete_student("students_collection", id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )

    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )

