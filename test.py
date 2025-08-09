from jsonschema import validate
from jsonschema.validators import Draft202012Validator

schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"}
    },
    "required": ["username"]
}

response = {
    "id": "12345",
    "email": "user-email",
    "age": 25
}

validate(instance=response, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER)