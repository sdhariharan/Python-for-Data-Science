def decorator1(func):
    def wrapper():
        print("func 1")
        func()
        print("func 1 end")

    return wrapper
def decorator2(func):
    def wrapper():
        print("func 2")
        func()
        print("func 2 end")

    return wrapper
@decorator1
def greet():
    print("Hariharan")
greet()

@decorator2
def greet2():
    print("Harikishan")
greet2()
