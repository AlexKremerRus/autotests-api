import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())


data = {
    "title": "new task 1",
    "completed": False,
    "userId":1

}

response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)

print(response.status_code)
print(response.request.headers)
print(response.json())

data = {"username":"test_user", "password":"123456"}

response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
print(response.request.headers)
print(response.json())

headers = {"Authorization":"my secret"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.request.headers)
print(response.json())


params= {"userId":1}
response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print("-------------------")
print(response.url)
print(response.json())


files = {"file":("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

print("-------------------")
print(response.url)
print(response.json())


with httpx.Client() as client:
    response1 = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = httpx.get('https://jsonplaceholder.typicode.com/todos/2')

print(response1.json())
print(response2.json())

client = httpx.Client(headers=headers)
response = client.get("https://httpbin.org/get")

print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos2sdfsdfsdf")
    response.raise_for_status()
    print(response.status_code)
except httpx.HTTPStatusError as e:
    print(f"error {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)

except httpx.ReadTimeout as e:
    print(f"error read timeout {e}")
