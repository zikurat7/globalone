print("Welcome to Zikurat!") #welcome message

def get_name(): #fuction to get a name of a person
    while True:
        name = input("What is ur name?").strip()
        if len(name) >= 2 and len(name) <=20:
            return name.strip()
        else:
            print("invalid name")

def get_age(): #fuction to get a age of a person
    while True:
        try:
            age = int(input("What is ur age?"))
            if age >= 0 and age <= 120:
                return age
            else:
                print("invalid age")
        except ValueError:
            print("invalid number")

def check_age(age): #function to check age eligibility
    if age < 18:
        return "access denied"
    elif age <=64:
        return "access granted"
    elif age <=120:
        return "old access granted"
    else:
        return "access denied"

def get_mail(): #function for email
    while True:
        mail = input("What is your email?").strip()
        if "@" in mail:
            return mail.strip()
        else:
            print("Wrong email")
    
user_name = get_name()
user_age = get_age()
status = check_age(user_age)
user_mail = get_mail()

print(status) #printing return value from check_age fuction
print(f"")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"email {user_mail}")