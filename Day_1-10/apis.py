import requests
# response= requests.get("https://jsonplaceholder.typicode.com/todos?userId=1")
# print(response.status_code)
# # print(response.text)
# data=response.json()

# for todo in data:
#     if todo["completed"]:
#         status = "Done"
#     else:
#         status = "Pending"

#     print(f"{todo['title']} - {status}")
params = {
    "userId": 1,
    "completed": True
}   
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params=params
)

print(response.url)

data = response.json()

for todo in data:
    print(todo["id"], todo["title"], todo["completed"])
print(response.url)
# title = data["title"]
# title = data["userId"]
# completed = data["completed"]
# if completed==True:
#     print("Done")
# else:
#     print("Still to do")
