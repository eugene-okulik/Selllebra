import sys


sys.set_int_max_str_digits(50000)


def fibonac():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


count = 0
for number in fibonac():
    count += 1
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
