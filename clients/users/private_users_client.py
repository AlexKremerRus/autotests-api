from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthentificationUserDict

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastname: str
    firstName: str
    middleName: str

class GetUseresponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user:User

class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_me(self) -> Response:
        response = self.get_user_me_api()
        return response.json()


    def get_user_api(self, user_id:str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def get_user(self, user_id:str) -> GetUseresponseDict:
        response = self.get_user_api(user_id)
        return response.json()

    def update_user_api(self, user_id:str, request: UpdateUserRequestDict) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id:str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")



def get_private_users_client(user: AuthentificationUserDict)->PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))