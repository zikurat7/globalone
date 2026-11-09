# name = ["Jack", "Kok", "Mom"]


# def greet(name, age, city):
#     print(f"My name is {name}, I'm {age} years old, i live in {city}!")

# greet("Valerii", 28, "Amsterdam")
# greet(age = 28, city = "Amsterdam", name = "Valerii")

# def introduce(name, age, city):
#     print(f"Hello my name {name}, i'm {age} years old, i live in {city}")
# introduce("Valerii", 28, "Amsterdam")

# def calculate_total(hours, rate, tax=10):
#     subtotal = hours * rate
#     taxtotal = subtotal * tax / 100
#     result = subtotal - taxtotal
#     print(f"Net salary: {result}")
# calculate_total(160, 15)
# calculate_total(hours = 160, rate = 15, tax = 20)


def show_user(**users):
    for key, value in users.items():
        print(f"{key}: {value}")


show_user(name="Alex", age=28, city="Amsterdam")
