import allure

from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from config import settings

from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("FILES_ASSERTIONS")  # Создаем логгер с именем "FILES_ASSERTIONS"

@allure.step("Проверка ответа создания файла")
def asser_create_file_response(request:CreateFileRequestSchema, response: CreateFileResponseSchema):
    logger.info("Проверка ответа создания файла")
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")
    assert_equal(str(response.file.url), expected_url, "url")

@allure.step("Проверка файла")
def assert_file(actual:FileSchema,expected: FileSchema ):
    logger.info("Проверка файла")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")

@allure.step("Проверка ответа получения файла")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    logger.info("Проверка ответа получения файла")
    assert_file(get_file_response.file, create_file_response.file)

@allure.step("Проверка ответа на создания файла с пустым именим")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    logger.info("Проверка ответа на создания файла с пустым именим")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Проверка ответа на создания файла с пустой директорией")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    logger.info("Проверка ответа на создания файла с пустой директорией")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Проверка ответа на создания файла с ненайденным файлом")
def assert_file_not_found_response(actual:InternalErrorResponseSchema):
    logger.info("Проверка ответа на создания файла с ненайденным файлом")
    expected =InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)

@allure.step("Проверка ответа на получения файла с некорректным айди")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    logger.info("Проверка ответа на получения файла с некорректным айди")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"},
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                location=["path", "file_id"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)