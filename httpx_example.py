import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "Новая задача",
#     "userId": 1,
#     "completed": False
# }
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
#
# print(response.status_code)
# print(response.json())
# print(response.request.headers)
#
# data = {
#     "username": "Nastya",
#     "password": "popatest"
# }
#
#
# # передача параметров через создание переменной со словарем
# params={"userId": 1}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
#
# print(response.url)
# print(response.json())
#
#
# # передача файлов
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.json())
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())
# print(response2.json())
#
#
# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# response = client.get("https://httpbin.org/get")
#
# print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=None)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
