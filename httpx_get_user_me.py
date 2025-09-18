import httpx

login_data = {
  "email": "polinam@example.com",
  "password": "12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_data)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status code:", login_response.status_code)

token= login_response_data['token']['accessToken']
headers = {"Authorization": f"Bearer {token}"}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Token response:", response.json())
print("Status code:", response.status_code)

