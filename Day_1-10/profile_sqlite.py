import sqlite3

# Connect to database
connection = sqlite3.connect("profile.db")

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL
    )
""")


def insert_profile():
    print("\nInserting Profile")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")

    cursor.execute("""
        INSERT INTO profiles (name, age, city)
        VALUES (?, ?, ?)
    """, (name, age, city))

    connection.commit()

    print("Profile inserted successfully!")

def view_profiles():
    cursor.execute("SELECT * FROM profiles")
    profiles=cursor.fetchall()
    for profile in profiles:
        print(profile)

def update_profiles():
    user_id = int(input("Enter ID to update: "))

    cursor.execute(
        "SELECT * FROM profiles WHERE id=?",
        (user_id,)
    )

    profile = cursor.fetchone()

    if profile is None:
        print("Profile not found.")
        return

    print("\nCurrent Profile:")
    print("ID:", profile[0])
    print("Name:", profile[1])
    print("Age:", profile[2])
    print("City:", profile[3])

    new_name = input("Enter new name (or press Enter to keep current): ")
    new_age = input("Enter new age (or press Enter to keep current): ")
    new_city = input("Enter new city (or press Enter to keep current): ")

    if new_name:
        name = new_name
    else:
        name = profile[1]

    if new_age:
        age = int(new_age)
    else:
        age = profile[2]

    if new_city:
        city = new_city
    else:
        city = profile[3]
    cursor.execute("""
        UPDATE profiles
        SET name=?, age=?, city=?
        WHERE id=?
    """, (name, age, city, user_id))

    connection.commit()

    print("\nProfile updated successfully!")

    print("Updated Profile:")
    print("Name:", name)
    print("Age:", age)
    print("City:", city)




def delete_profile():
    user_id = int(input("Enter ID to delete: "))

    cursor.execute(
        "SELECT * FROM profiles WHERE id=?",
        (user_id,)
    )

    profile = cursor.fetchone()

    if profile is None:
        print("Profile not found.")
        return

    cursor.execute(
        "DELETE FROM profiles WHERE id=?",
        (user_id,)
    )

    connection.commit()

    print("\nProfile deleted successfully!")
while True:
    print("\n1. Insert Profile")
    print("2. Update Profile")
    print("3. View Profile")
    print("4. Delete Profile")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_profile()
    elif choice == "2":
        update_profiles()
    elif choice == "3":
        view_profiles()
    elif choice == "4":
        delete_profile()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")




connection.close()