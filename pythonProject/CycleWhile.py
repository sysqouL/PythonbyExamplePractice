# -------------------------------------------
""" Exercise 45
total = 0
while total <= 50:
    num = int(input("Введите число: "))
    total = total + num
    print("The total is ",total)
"""



"""
# -------------------------------------------
# Exercise 46
num = 0
while num <= 5:
    num = int(input("Введите число: "))
print("The last number you entered was a ",num)
"""



""" 
# -------------------------------------------
# Exercise 47
num1 = int(input("Введите первое число - "))
result = num1
again = "yes"
while again == "yes":
    num2 = int(input("Введите второе число - "))
    result = result + num2
    again = input("Продолжаем - yes/no ? ")
print("Сумма - ",result)
"""


"""
# -------------------------------------------
# Exercise 48
count = 0
moore = "yes"
while moore == "yes":
    name = input("Введите Имя - ")
    print(name, "был приглашен")
    count = count + 1
    moore = input("Пригласить еще ? yes/no - ")
print("Количество приглашённых - ",count)
"""


"""
# -------------------------------------------
# Exercise 49
compnum = 50
num = int(input("Введите число - "))
count = 1
while num != compnum:
    if num <compnum:
        print("Введенное число меньше 50")
    else:
        print("Введенное число больше 50")
    count = count + 1
    num = int(input("Введите еще число - "))
print("Числа совпали, количество попыток - ",count)
"""


"""
# -------------------------------------------
# Exercise 50
number1 = int(input("Введите число от 10 до 20: "))
while number1 < 10 or number1 > 20:
    if number1 >= 10:
        print("Много")
    else:
        print("Мало")
    number1 = int(input("Введите число еще раз - "))
print("OK")
"""


"""
# -------------------------------------------
# Exercise 51
count = 10
while count > 0:
    print("There are ",count, "green bottles hanging on the wall")
    print(count, "green bottles hanging on the wall")
    print("and if 1 green bottle should accidentally fall")
    count = count - 1
    answer = int(input("How many green bottles will be hanging on the wall? "))
    if answer == count:
        print("There will be ", count, "green bottles")
    else:
        while answer != count:
            answer = int(input("Try again: "))
print("OK")
"""


