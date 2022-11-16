import motor.motor_asyncio
from app.server.configs import MONGO_URL
from bson import ObjectId


class AsyncMongoConnect:
    def __init__(self, database):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
        self.db = self.client[database]

    # Retrieve all students present in the database
    async def retrieve_students(self, table_name: str):
        collection = self.db[table_name]
        students = []
        try:
            async for student in collection.find({}, {"_id": 0}):
                students.append(student)
            return students
        except Exception as e:
            print(f"Error: {e}")

    # add a new student into to the database
    async def add_student(self, table_name: str, student_data: dict):
        collection = self.db[table_name]
        student = await collection.insert_one(student_data)
        return str(student.inserted_id)

    # retrieve a student with a matching ID
    async def retrieve_student(self, table_name: str, id: str) -> dict:
        collection = self.db[table_name]
        student = await collection.find_one({"_id": ObjectId(id)})
        if student:
            student["_id"] = str(student["_id"])
            return student

    # Update a student with a matching ID
    async def update_student(self, tablename: str, id: str, data: dict):
        collection = self.db[tablename]
        # Return false if a empty request body is sent.
        if len(data) < 1:
            return False

        # check student exists hay chua
        student = await collection.find_one({"_id": ObjectId(id)})
        if student:
            updated_student = await collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_student:
                return True
            return False

    # Delete a student from the database
    async def delete_student(self, table_name: str, id: str):
        collection = self.db[table_name]
        student = await collection.find_one({"_id": ObjectId(id)})
        if student:
            await collection.delete_one({"_id": ObjectId(id)})
            return True