import sys 
import requests 

todo_id = sys.argv[1]
url =f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

try:
    response= requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    print(f"ID: {data['id']}")
    
    print(f"Title: {data['title']}")
    
    if data["completed"]:
        print("Status : Done")
    else:
        print("Status: Pending")
except requests.HTTPError:
    print("Todo not found.")