def decider(func):
    def wrapper(num1, num2):
        if num1 < 0 or num2 < 0:
            operation = "*"
        elif num1 < num2:
            operation = "/"
        elif num1 == num2:
            operation = "+"
        elif num1 > num2:
            operation = "-"
        return func(num1, num2, operation)
    return wrapper


@decider
def calc(a, b, c):
    if c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    elif c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)


first, second = map(int, input("Add two numbers: ").split())

calc(first, second)
