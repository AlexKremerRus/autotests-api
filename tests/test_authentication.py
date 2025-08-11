from clients.authentification.authentification_client import get_authentification_client
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from clients.private_http_builder import AuthentificationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus

from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response


def test_login():
    public_users_client = get_public_users_client()

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)

    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data )

    validate_json_schema(response.json(), response_data.model_json_schema())


    login_request = LoginRequestSchema(email=request.email, password=request.password)

    authentication_client = get_authentification_client()

    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())




