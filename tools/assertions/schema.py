from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict ) -> None:
    """
    Проверяет соответствует ли объект заданной схеме
    :param instance:
    :param schema:

    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )