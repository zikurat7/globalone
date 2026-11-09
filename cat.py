first = "hello python" * 100000
second = "hello python" * 100000

print(id(first))
print(id(second))

print(f"Hello, {first}")


def hello():
    print("hello")
