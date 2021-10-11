
# ----------------------------------------------
"""
# 52 Exercise
import random
num = random.randint(1, 100)
print(num)
"""
# ----------------------------------------------


# ----------------------------------------------
"""
# 53 Exercise
import random
frukt = random.choice(["апельсин", "мандарин", "банан", "яблоко", "персик"])
print(frukt)
"""
# ----------------------------------------------


# ----------------------------------------------
"""
# 54 Exercise
import random
znach = random.choice(["ОРЁЛ", "РЕШКА"])
ygad = input("Угадайте значение - ОРЁЛ или РЕШКА: ")
if ygad == znach:
    print("Угадали !!!")
else:
    print("Нет (((")
print("Загаданное - ", znach)
"""
# ----------------------------------------------


# ----------------------------------------------
"""
# 55 Exercise
import random
num = random.randint(1, 5)
quess = int(input("Выберете число от 1 до 5: "))
if quess == num:
    print("Вы угадали !!!")
elif quess < num:
    quess = int(input("Введеное число меньше загаданного. Введите другое: "))
    if quess == num:
        print("Вы угадали !!!")
    else:
        print("Вы не угадали =(")
elif quess > num:
    quess = int(input("Введенное число больше загаданного. Введите другое: "))
    if quess == num:
        print("Вы угадали !!!")
    else:
        print("Вы не угадали =(")
"""
# ----------------------------------------------


# ----------------------------------------------
""" 
# 56 Exercise
import random
num = random.randint(1, 10)
chislo = int(input("Введите число от 1 до 10: "))
correct = False
while correct == False:
    chislo = int(input("Неугадали.Введите число от 1 до 10: "))
    if chislo == num:
        correct = True
        print("Вы угадали число !!!")
"""
# ----------------------------------------------


# ----------------------------------------------
"""
# 57 Exercise
import random
num = random.randint(1, 10)
chislo = int(input("Введите число от 1 до 10: "))
correct = False
while correct == False:
    chislo = int(input("Неугадали.Введите число от 1 до 10: "))
    if chislo == num:
        correct = True
        print("Вы угадали число !!!")
    elif chislo > num:
        print("Слишком много")
    else:
        print("Слишком мало")
"""
# ----------------------------------------------


# ----------------------------------------------
""" 
# 58 Exercise
import random
score = 0
for i in range(1, 6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    answer = int(input("Введите число: "))
    print()
    if answer == correct:
        score = score + 1
print("Количество баллов - ", score)
"""
# ----------------------------------------------

# ----------------------------------------------
""" 
# 59 Exercise
import random

colour = random.choice(["красный","жёлтый","зелёный","синий","белый"])
correct = True
while correct == True:
    yourcolour = input("Выберите цвет - красный,жёлтый,зелёный,синий или белый: ")
    yourcolour = yourcolour.lower()
    if yourcolour == colour:
        print("Ваш выбор совпал")
        break
    else:
        if colour == "красный":
            print("Запрещающий сигнал светофора")
        elif colour == "жёлтый":
            print("Лимон - ")
        elif colour == "зелёный":
            print("Огурец - ")
        elif colour == "белый":
            print("Молоко - ")
        elif colour == "синий":
            print("Стержень ручки - ")
# ----------------------------------------------
"""