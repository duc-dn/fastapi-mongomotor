from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    # example mo ta cho student schema
    # Tu dong tao 1 example trong api
    class Config:
        schema_extra = {
            "example": {
                "fullname": "Duc",
                "email": "ducdo@gmail.com",
                "course_of_study": "math",
                "year": 2,
                "gpa": "3.5"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}