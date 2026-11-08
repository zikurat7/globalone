print("List of users:") 
users = ["Alex", "John", "Max"] #[]this is list

for user in users:
    print(user)

new_user = input("Enter name to add: ").strip()
users.append(new_user)
new_user = input("Enter name to add: ").strip()
users.append(new_user)
def rem(): #function to remove user
    while True:
        try:
            remove_user = input("Enter name to delete: ").strip()
            if not remove_user:
                print("Name cannot be empty!")
                continue
            users.remove(remove_user)
            print(f"User {remove_user} deleted!")
            break
        except ValueError:
            print("invalid user!")
rem()

numbers = len(users)
print(f"List of users: {users}")
print(f"Number of users: {numbers}")