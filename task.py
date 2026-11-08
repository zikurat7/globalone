# numbers = [10, 20, 30, 40, 50]

# def num_add():
#     new_number = int(input("Add number:"))
#     numbers.append (new_number)

# num_add()

# def num_rem():
#     del_number = int(input("Delete number:"))
#     numbers.remove (del_number)

# num_rem()
# print(f"List: {numbers}")
# first = numbers[0]
# print(first)

# for i in range(5):
#     print(i)

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#         print(fruit)

# number = 1
# while number <=15:
#     print(number)
#     number += 1

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# user = {
#     "name": "Alex",
#     "age": 28,
#     "city": "Amsterdam"
# }

# print(user["name"])

# user["job"] = "Developer"
# print(user["job"])
# user["age"] = 29
# print(user["age"])

# for key, value in user.items():
#     print(key, value)

# def multiply(a, b):
#     return a * b
# result = multiply(3, 5)
# print(f"answer: {result}")

def birtdate(birth_year):
    age = 2026 - birth_year
    return age
user_age = birtdate(2012)
if user_age >= 18:
    print("ur adult")
else:
    print("ur a kid")

print(f"Your age: {user_age}")