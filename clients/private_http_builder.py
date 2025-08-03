from httpx import Client

from clients.authentification.authentification_client import get_authentification_client, LoginRequestDict
from typing import TypedDict

class AuthentificationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthentificationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authorization_client = get_authentification_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authorization_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )
