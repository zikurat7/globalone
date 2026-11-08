print("List of users:") 
users = ["Alex", "John", "Max"] #[]this is list

for user in users:
    print(user)

def add(): #function to add 2 users
    while True:
        new_user = input("Enter name to add: ").strip()
        if not new_user:
            print("Name cannot be empty!")
            continue
        if new_user in users:
            print("This user already exist")
            continue
        users.append(new_user)
        print(f"New user {new_user} was added!")
        break

def rem(): #function to remove user
    while True:
        remove_user = input("Enter name to delete: ").strip()

        if remove_user == "exit":
            print("Deletion stopped!")
            break

        if not remove_user:
            print("Name cannot be empty!")
            continue

        if remove_user in users:
            users.remove(remove_user)
            print(f"User {remove_user} deleted!")

        else:
            print("invalid user!")

add()
add()
rem()

numbers = len(users)
print(f"\nList of users: {users}")
print(f"Number of active users: {numbers}")