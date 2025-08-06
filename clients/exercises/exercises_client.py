from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import get_private_http_client, AuthentificationUserDict

class GetExercisesQueryDict(TypedDict):
    courseId: str

class Exercise(TypedDict):
    """
    Описание структуры.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания.
    """
    exercises: Exercise

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания..
    """
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: Exercise

class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str

class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        return self.get("/api/v1/exercises", params=query)

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        return self.post("/api/v1/exercises",json=request)

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict ):
        return self.patch(f"/api/v1/exercises/{exercise_id}",json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict ) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise_api(self, exercise_id:str):
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_exercises_client(user: AuthentificationUserDict)->ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))