
""" ------------------------------------------
# 35 Exercise

name = input("Введите свое имя - ")
for i in range(0, 3):
    print(name)
"""


""" ------------------------------------------
# 36 Exercise
name = input("Введите свое имя -")
count = int(input("Введите количество повторений - "))
for i in range(0, count):
    print(name)
"""


""" ------------------------------------------
# 37 Exercise
name = input("Введите имя - ")
for i in name:
    print(i)
"""


""" ------------------------------------------
# 38 Exercise
name = input("Введите имя -")
count = int(input("Введите количество повторений - "))
for x in range(0, count):
    for i in name:
        print(i)
"""


""" ------------------------------------------
# 39 Exercise
count = int(input("Введите число от 1 до 12 - "))
for i in range(1,13):
    answer = i * count
    print(i, "x", count, "=", answer)
"""


""" ------------------------------------------
# 40 Exercise
number = int(input("Введите число до 50 - "))
for i in range( 50, number-1, -1):
    print(i)
"""


""" ------------------------------------------
# 41 Exercise
number = int(input("Введите число - "))
name = input("Введите Имя - ")
if number < 10:
    for i in range(0, number):
        print(name)
else:
    for i in range(0, 3):
        print("Too high")
"""


""" ------------------------------------------
# 42 Exercise
total = 0
for i in range(0, 5):
    number = int(input("Введите число: "))
    ans = input("Включить введённое число в суммирование ? yes/no - ")
    if ans == "yes":
        total = total + number
print(total)
"""


""" ------------------------------------------
# 43 Exercise
napravlenie = input("Введите направление отсчёта - прямое/обратное: ")
if napravlenie == "прямое":
    number = int(input("Введите число: "))
    for i in range(1, number+1):
        print(i)
elif napravlenie == "обратное":
    number = int(input("Введите число меньше 20: "))
    for i in range(20,number-1,-1):
        print(i)
else:
    print("Ошибка")
"""


""" ------------------------------------------
# 44 Exercise
count_people = int(input("Введите количество гостей: "))
if count_people < 10:
    for i in range(0, count_people):
        name = input("Введите имя: ")
        print(name, "has been invited")
else:
    print("Too many people")
"""

