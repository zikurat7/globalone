print("Hello, Zikurat!") #welcome message
name = input("What is ur name?")
while True:
    try:
        age = int(input("What is ur age?"))
        if age < 0:
            print("invalid age")
        else: 
            break
    except ValueError:
        print("invalid number")
if age < 18:
    print("access denied")
elif age <=64:
    print("access granted")
else:
    print("senior access granted")
print(f"Hello, {name}, you are {age} years old.")