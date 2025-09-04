
from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import get_private_http_client, AuthentificationUserSchema
from clients.exercises.exercises_schema import (GetExercisesQuerySchema,
                                                GetExercisesResponseSchema,
                                                GetExerciseResponseSchema,
                                                CreateExercisesRequestSchema,
                                                CreateExerciseResponseSchema,
                                                UpdateExercisesRequestSchema,
                                                UpdateExerciseResponseSchema
                                                )

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        return self.post("/api/v1/exercises",json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestSchema ):
        return self.patch(f"/api/v1/exercises/{exercise_id}",json=request.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestSchema ) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id:str):
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_exercises_client(user: AuthentificationUserSchema)->ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))