print("Welcome to Zikurat!") #welcome message

def get_name(): #fuction to get a name of a person
    while True:
        name = input("What is ur name?").strip()
        if len(name) > 2 and len(name) <20:
            return name.strip()
        else:
            print("invalid name")

def get_age(): #fuction to get a age of a person
    while True:
        try:
            age = int(input("What is ur age?"))
            if age < 0:
                print("invalid age")
            else: 
                return age
        except ValueError:
            print("invalid number")

def check_age(age): #function to check age eligibility
    if age < 18:
        return "access denied"
    elif age <=64:
        return "access granted"
    else:
        return "senior access granted"

user_name = get_name()
user_age = get_age()
status = check_age(user_age) 

print(status) #printing return value from check_age fuction
print(f"Hello, {user_name}, you are {user_age} years old.") #end message