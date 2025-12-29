import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

user_id = requests.get(api_url).json().get("userId")

if user_id in [100, 200, 300]:
    print("User found")
