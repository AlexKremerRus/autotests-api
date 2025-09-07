from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("SCHEMA_ASSERTIONS")

@allure.step("Валидация JSON Схемы")
def validate_json_schema(instance: Any, schema: dict ) -> None:
    """
    Проверяет соответствует ли объект заданной схеме
    :param instance:
    :param schema:

    """
    logger.info("Validating JSON schema")
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )