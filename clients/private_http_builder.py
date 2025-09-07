from httpx import Client
from pydantic import BaseModel, EmailStr, ConfigDict
from clients.authentification.authentification_client import get_authentification_client
from functools import lru_cache
from clients.authentification.authentification_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings

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
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],  # Логируем исходящие HTTP-запросы
            "response": [log_response_event_hook]  # Логируем полученные HTTP-ответы
        },
    )
