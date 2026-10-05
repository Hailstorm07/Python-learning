# pyright: reportShadowedImports=false
import json
def get_age():
    while True:
        try:
            age=int(input("Enter your age:"))
            if age <0:
                print("Age cannot be negative")
                continue
            return age
        except(ValueError):
            print("Enter valid age")
    
def insert_profile():
    print("Inserting Profile")
    name = input("Enter your name: ")
    age = get_age()
    city = input("Enter your city: ")
    new_profile = {
            "name": name,
            "age": age,
            "city": city
        }
    with open("profile.json", "r") as file:
        profiles = json.load(file)
        profiles.append(new_profile)
    with open("profile.json", "w") as file:
        json.dump(profiles, file, indent=4)
    print("Profile inserted successfully!")

def update_profile():
    print("Updating Profile")
    with open("profile.json",'r') as file:
        profiles = json.load(file)
        for index, profile in enumerate(profiles):
            print(f"{index + 1}. Name: {profile['name']}, Age: {profile['age']}, City: {profile['city']}")
        print("Enter the index of the profile you want to update (1 to {}):".format(len(profiles)))
        index = int(input()) - 1
        if index < 0 or index >= len(profiles):
            print("Invalid index. Please try again.")
            return  
        profile = profiles[index]
        print("Enter new details (leave blank to keep current value):")
        new_name = input("Enter new name (or press Enter to keep current): ")
        new_age = int(input("Enter new age (or press Enter to keep current): "))
        new_city = input("Enter new city (or press Enter to keep current): ")

        if new_name:
            profile["name"] = new_name
        if new_age:
            profile["age"] = int(new_age)
        if new_city:
            profile["city"] = new_city

        with open("profile.json", 'w') as file:
            json.dump(profiles, file)
        print("Profile updated successfully!")
        
def delete_profile():
        print("Deleting Profile")
        with open("profile.json", 'r') as file:
            profiles=json.load(file)
            for index, profile in enumerate(profiles):
                print(
                    f"{index+1}. Name:{profile['name']},"
                    f"Age:{profile['age']},"
                    f"City:{profile['city']}"
                )
            index = int(input("Enter the profile number to delete")) -1
            if index <0 or index>=len(profiles):
                print("Invalid profile number")
            else:
                deleted_profile=profiles.pop(index)
                with open('profile.json',"w") as file:
                    json.dump(profiles, file, indent=4)
                print("profile deleted successfully")
                print("Deleted:",deleted_profile)
        
        
def search_profile():
    print("Searching Profile")

    with open("profile.json", "r") as file:
        profiles = json.load(file)

    search_name = input("Enter name to search: ")
    found = False

    for profile in profiles:
        if profile["name"].lower() == search_name.lower():
            print(
                    f"Name: {profile['name']}, "
                    f"Age: {profile['age']}, "
                    f"City: {profile['city']}"
                )
            found = True

    if not found:
        print("No profile found.")
    
def view_profiles():
    print("Viewing")
    with open("profile.json", 'r') as file:
        profiles= json.load(file)
        for profile in profiles:
            print("Profile:")
            print("Name:", profile["name"])
            print("Age:", profile["age"])
            print("City:", profile["city"])

while True:
    print("\n1. Insert Profile")
    print("2. Update Profile")
    print("3. View Profile")
    print("4. Delete Profile")
    print("5. Search Profile")
    print("6. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        insert_profile()

    elif ch == 2:
        update_profile()

    elif ch == 3:
        view_profiles()

    elif ch == 4:
        delete_profile()

    elif ch == 5:
        search_profile()

    elif ch == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")