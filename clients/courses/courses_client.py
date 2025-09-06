import allure
from httpx import Response

from clients.api_client import APIClient

from clients.private_http_builder import AuthentificationUserSchema, get_private_http_client
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCoursesRequestSchema, CreateResponseSchema, UpdateCoursesRequestSchema

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    @allure.step("Получение курсов")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
         Метод получения списка курсов.

         :param query: Словарь с userId.
         :return: Ответ от сервера в виде объекта httpx.Response
         """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    @allure.step("Получение курса по айди {course_id}")
    def get_course_api(self, course_id:str) -> Response:
        """
         Метод получения курса.

         :param course_id: Идентификатор курса.
         :return: Ответ от сервера в виде объекта httpx.Response
         """
        return self.get(f"/api/v1/courses/{course_id}")

    @allure.step("Создание курса")
    def create_courses_api(self, request: CreateCoursesRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    @allure.step("Создание курса")
    def create_course(self, request:CreateCoursesRequestSchema) -> CreateResponseSchema:
        response = self.create_courses_api(request)
        return CreateResponseSchema.model_validate_json(response.text)

    @allure.step("Обновление курса по айди {course_id}")
    def update_course_api(self,course_id: str, request: UpdateCoursesRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Удаление курса по айди {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

def get_courses_client(user: AuthentificationUserSchema)->CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))