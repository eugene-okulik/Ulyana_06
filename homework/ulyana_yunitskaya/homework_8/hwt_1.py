import random


bonus = random.choice([True, False])
salary = int(input('What is your salary?'))

if bonus is True:
    print(f"{salary}, True - '${salary + random.randint(10, 1000)}'", sep =', ')
else:
    print(f"{salary}, False - '${salary}'", sep =', ')
