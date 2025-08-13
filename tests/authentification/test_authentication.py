import pytest

from clients.authentification.authentification_client import AuthentificationClient
from clients.authentification.authentification_schema import LoginRequestSchema, LoginResponseSchema
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code

@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentification:
    def test_login(self, function_user: UserFixture, authentification_client: AuthentificationClient):
        login_request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        login_response = authentification_client.login_api(login_request)
        login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

        assert_status_code(login_response.status_code, HTTPStatus.OK)
        assert_login_response(login_response_data)

        validate_json_schema(login_response.json(), login_response_data.model_json_schema())


