from clients.api_client import APIClient

from httpx import Response

from typing import TypedDict

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса по созданию users.
    """
    email: str
    password: str
    lastname: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastname, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
