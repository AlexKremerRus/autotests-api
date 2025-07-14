import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

headers ={"Authorization":f"Bearer {login_response_data['token']['accessToken']}"}

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
users_me_response_data = users_me_response.json()

print(users_me_response.status_code)
print(users_me_response_data)