from clients.courses.courses_client import CoursesClient, get_courses_client
import pytest
from pydantic import BaseModel
from clients.courses.courses_schema import CreateCoursesRequestSchema, CreateResponseSchema
from fixtures.users import UserFixture
from fixtures.file import FileFixture

class CourseFixture(BaseModel):
    request: CreateCoursesRequestSchema
    response: CreateResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentification_user)

@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file:FileFixture
) -> CourseFixture:
    request = CreateCoursesRequestSchema(
        previewFileId=function_file.response.file.id,
        createdByUserId=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)