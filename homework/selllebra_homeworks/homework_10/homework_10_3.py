def decider(func):
    def wrapper(num1, num2, oper):
        if num1 < 0 or num2 < 0:
            print("Сработал decider:", num1 * num2)
        elif num1 < num2:
            print("Сработал decider:", num1 / num2)
        elif num1 == num2:
            print("Сработал decider:", num1 + num2)
        elif num1 > num2:
            print("Сработал decider:", num1 - num2)
        else:
            func(num1, num2, oper)
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

calc(first, second, "+")
