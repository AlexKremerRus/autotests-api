from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

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

    def get_exercises_api(self, query: str) -> Response:
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        return self.post("/api/v1/exercises",json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict ):
        return self.patch(f"/api/v1/exercises/{exercise_id}",json=request)

    def delete_exercise_api(self, exercise_id:str):
        return self.delete(f"/api/v1/exercises/{exercise_id}")

