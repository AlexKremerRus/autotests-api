import allure

from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("ERRORS_ASSERTIONS")

@allure.step("Проверка валидационной ошибки")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    logger.info("Проверка валидационной ошибки")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")

@allure.step("Проверка ответа валидационной ошибки")
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    logger.info("Проверка валидационной ошибки")

    assert_length(actual.details, expected.details, "details")
    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail )

@allure.step("Проверка внутренней ошибки ответа")
def assert_internal_error_response(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    logger.info("Проверка внутренней ошибки ответа")
    assert_equal(actual.details, expected.details, "details")






