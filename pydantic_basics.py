"""
 {
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr
from pydantic.alias_generators import to_camel

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name:str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id:str = Field(default_factory=lambda: str(uuid.uuid4()))
    title:str = "Playwright"
    max_score:int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "Playwright course test"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 week")
    created_by_user:UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="testttt",
    previewFile=FileSchema(
        id = "file_id",
        filename="file.png",
        directory="courses",
        url="http://localhost:8000"
    ),
    estimatedTime='1 week',
    createdByUser = UserSchema(
        id="user_id",
        email="user@mail.ru",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice "
    )
)

print(course_default_model)

course_dict = {
    "id": "course2",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "testttt",
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "directory": "tese",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
      "id": "user-id",
      "email": "user@example.com",
      "lastName": "test",
      "firstName": "test2",
      "middleName": "nhehhe"
    }
}

course_dict_model = CourseSchema(**course_dict)

print(course_dict_model)

course_json = """
{
    "id": "course1",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "testttt",
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "directory": "tese",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
      "id": "user-id",
      "email": "user@example.com",
      "lastName": "test",
      "firstName": "test2",
      "middleName": "nhehhe"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)

print(course_json_model)

print(course_json_model.model_dump(by_alias=True), type(course_json_model.model_dump()))
print(course_json_model.model_dump_json(by_alias=True), type(course_json_model.model_dump_json()))

# course = CourseSchema()
# print("------____-------")
# print(course)
#
# course2 = CourseSchema()
# print("------____-------__ ")
# print(course2)

user = UserSchema(

      id= "user-id",
      email= "user@example.com",
      lastName= "test",
      firstName= "test2",
      middleName= "nhehhe"

)

print(user)

file = FileSchema(
        id= "file-id",
        filename= "file.png",
        directory= "tese",
        url= "http://localhost:8000"
)

print(file)
