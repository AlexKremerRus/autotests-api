from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
import pytest

from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExerciseResponseSchema
from pydantic import BaseModel

class ExerciseFixture(BaseModel):
    request: CreateExercisesRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentification_user)

@pytest.fixture
def exercises_file(exercises_client: ExercisesClient,
        function_course: CourseFixture) -> ExerciseFixture:
    request = CreateExercisesRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)