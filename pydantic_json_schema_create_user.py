from clients.private_http_builder import AuthentificationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from tools.fakers import get_random_email
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema

from tools.assertions.schema import validate_json_schema


public_user_clients = get_public_users_client()


create_user_request = CreateUserRequestSchema(
    email= get_random_email(),
    password= "string",
    last_name= "string",
    first_name= "string",
    middle_name= "string",
)

create_user_response = public_user_clients.create_user_api(create_user_request)

# print(create_user_response.json())
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

user = AuthentificationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)


private_users_client = get_private_users_client(user)

get_user_request = private_users_client.get_user_api(create_user_response.json()['user']['id'])
print("_____-----_____")
print(get_user_request.json())


get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_request.json(), schema=get_user_response_schema)

