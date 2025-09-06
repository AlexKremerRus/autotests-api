import allure

from clients.api_client import APIClient
from httpx import Response

from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema
from clients.private_http_builder import get_private_http_client, AuthentificationUserSchema

class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    @allure.step("Получение данных о моем юзере")
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    @allure.step("Получение данных о моем юзере")
    def get_user_me(self) -> Response:
        response = self.get_user_me_api()
        return response.json()

    @allure.step("Получение юзера по его айди {user_id}")
    def get_user_api(self, user_id:str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    @allure.step("Получение юзера по его айди {user_id}")
    def get_user(self, user_id:str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    @allure.step("Обновление юзаре по айди {user_id}")
    def update_user_api(self, user_id:str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    @allure.step("Удаление пользователя по айди {user_id}")
    def delete_user_api(self, user_id:str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

def get_private_users_client(user: AuthentificationUserSchema)->PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))