import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal

@allure.step("Проверка ответа создание пользователя")
def assert_create_user_response(request:CreateUserRequestSchema, response:CreateUserResponseSchema):
    assert_equal( response.user.email, request.email, 'email')
    assert_equal( response.user.last_name, request.last_name, 'last_name')
    assert_equal( response.user.first_name, request.first_name, 'first_name')
    assert_equal( response.user.middle_name, request.middle_name, 'middle_name')

@allure.step("Проверка пользователя")
def assert_user(actual:UserSchema, expected:UserSchema):
    assert_equal( actual.id, expected.id, 'id')
    assert_equal( actual.email, expected.email, 'email')
    assert_equal( actual.last_name, expected.last_name, 'last_name')
    assert_equal( actual.first_name, expected.first_name, 'first_name')
    assert_equal( actual.middle_name, expected.middle_name, 'middle_name')

@allure.step("Проверка ответа на получения пользователя")
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    assert_user(get_user_response.user, create_user_response.user)
