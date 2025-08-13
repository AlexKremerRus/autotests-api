from clients.private_http_builder import AuthentificationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from tools.fakers import fake
from clients.users.users_schema import CreateUserRequestSchema

public_user_clients = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email= fake.email(),
    password= "string",
    last_name= "string",
    first_name= "string",
    middle_name= "string",
)

create_user_response = public_user_clients.create_user(create_user_request)
print(create_user_response)


authentification_user = AuthentificationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentification_user)
get_user_response = private_users_client.get_user(create_user_response.user.id)

print(get_user_response)
