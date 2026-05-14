text = "результат операции: 22"

def number_increase(line):
    list_from_line = line.split(" ")
    return int(list_from_line[-1]) + 10


print(number_increase(text))
