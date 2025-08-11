import pytest

from clients.authentification.authentification_client import get_authentification_client, AuthentificationClient
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus

from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response

@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user:UserFixture, authentification_client:AuthentificationClient):

    login_request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    login_response = authentification_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())




