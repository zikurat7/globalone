print("Hello, Zikurat!") #welcome message
name = input("What is ur name?")
age = int (input("What is ur age?"))
if age < 0:
    print("error")
elif age < 18:
    print("kid")
elif age >= 18 and age <=64:
    print("normal")
else:
    print("old fart")
print(name)