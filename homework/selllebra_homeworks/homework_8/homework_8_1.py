import random


salary = int(input('Write your salary'))
bonus = random.choice([True, False])
result = salary
if bonus == True:
    result = (salary + random.randrange(10, 10000, 100))
print(f"{salary}, {bonus} - '${result}'")
