import requests

print("=== Todo API Explorer ===")
while True:
    try:
        user_id = int(input("Enter User ID (1-10): "))
        if 1<=user_id<=10:
            break
        print("Please enter a number between 1-10: ")
    except ValueError:
        print("Pleaseenter a valid number")
        
params = {
    "userId": user_id
}
try:
    response = requests.get(
                "https://jsonplaceholder.typicode.com/todos",
                params=params,
                timeout=5
    )
    response.raise_for_status()
    todos=response.json()
except requests.Timeout:
    print("Connection timed out")
except requests.ConnectionError:
    print("Connection error")
except requests.HTTPError:
    print("API returned an HTTP error")
except requests.RequestException:
    print("An error encountere")
        
    
else:
    print(f"Found {len(todos)} todos.")

    choice = input("Show (a)ll, (c)ompleted, or (p)ending? ").lower()
    while choice not in ("a", "c", "p"):
        print("Invalid choice. Please enter a, c, or p.")
        choice = input("Show (a)ll, (c)ompleted, or (p)ending? ").lower()
    for todo in todos:

        if choice == "c" and not todo["completed"]:
            continue

        if choice == "p" and todo["completed"]:
            continue

        status = "Done" if todo["completed"] else "Pending"
        print(f"{todo['id']}. {todo['title']} - {status}")
        
