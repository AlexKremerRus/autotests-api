import httpx
from tools.fakers import get_random_email

#Create User
create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

#Authorization
login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

#Update user
update_user_payload = {
  "email": get_random_email(),
  "lastName": "test2",
  "firstName": "test3",
  "middleName": "test4"
}

update_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
update_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=update_user_headers,
    json=update_user_payload
)
update_response_data = update_response.json()
print(update_response.status_code)
print(update_response_data)