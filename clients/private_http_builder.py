from httpx import Client
from pydantic import BaseModel, EmailStr, ConfigDict
from clients.authentification.authentification_client import get_authentification_client
from functools import lru_cache
from clients.authentification.authentification_schema import LoginRequestSchema

class AuthentificationUserSchema(BaseModel):
    model_config = ConfigDict(frozen=True)  # V2 стиль
    email: EmailStr
    password: str

@lru_cache(maxsize=None)
def get_private_http_client(user: AuthentificationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authorization_client = get_authentification_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authorization_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
