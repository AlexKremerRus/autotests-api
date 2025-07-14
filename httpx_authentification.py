import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response_data)
print(login_response.status_code)

refresh_payload = {
"refreshToken": login_response_data['token']['refreshToken']
}

refresh_payload = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_payload_data = refresh_payload.json()

print(refresh_payload_data)
print(refresh_payload.status_code)
