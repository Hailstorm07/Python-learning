import requests
try:
    response=requests.get("https://jsonplaceholder.typicode.com/todos/9999")
    response.raise_for_status()
    print(response.status_code)
except requests.HTTPError:
    
    print("Not Found: 404")