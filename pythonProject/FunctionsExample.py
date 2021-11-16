# ---------------------------------------
"""                                   """


"""
# Использование подпрограмм
"""

"""
    def get_data():
        user_name = input("Введите имя: ")
        user_age = int(input("Введите возраст: "))
        data_tuple = (user_name, user_age)
        return data_tuple                           -   return может содержать только одно значение, поэтому 2 перенные объедененны в кортеж data_tuple
        
    def message(user_name, user_age):  -  подпрограмма message(), которая использует 2 ранее опреденные перменные
        if user_age > 10:
         print("Hello ", user_name)
         
    def main():                           -  подпрограмма main(), которая получает 2 перменные от get_data(). Перменные должны следовать в том порядке,  котором они определены ранее в кортеже. Затем вызывается message()
        user_name, user_age = get_data()
        message(user_name, user_age)     
    
    main()  -  запускает подпрограмму main() 
"""


# ---------------------------------------
"""
# 118 Пример с числами с использованием подпрограмма

def get_num():
    num = int(input("Введите число: "))
    return num

def reverse(num):
    n = 1
    while n <= num:
        print(n)
        n = n + 1
        
def main():
    num = get_num()
    reverse(num)

main()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 119 Угадываем числа

import random

def generation():
    num_small = int(input("Введите маленькое число: "))
    num_big = int(input("Введите большое число: "))
    comp_num = random.randint(num_small,num_big)
    return comp_num

def guessing():
    print("Я думаю что было загадано ... ")
    guess = int(input("Число: "))
    return guess

def result(comp_num,guess):
    again = True
    while again == True:
        if comp_num == guess:
            print("Вы УГАДАЛИ !!!")
            again = False
        elif comp_num > guess:
            guess = int(input("Слишком маленькое число, попробуйте снова: "))
        else:
            guess = int(input("Слишком большое число, попробуйте снова: "))

def main():
    comp_num = generation()
    guess = guessing()
    result(comp_num,guess)

main()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 120 Сложение, вычитание

import random

def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1, "+",num2, "= ")
    user_answer = int(input("Введите ваш ответ - "))
    actual_answer = num1 + num2
    print("Ваш ответ - ",user_answer)
    print("Правильный ответ - ",actual_answer)
    answers = (user_answer, actual_answer)
    return answers

def subtraction():
    num3 = random.randint(25,50)
    num4 = random.randint(1,25)
    print(num3, "-",num4, "= ")
    user_answer = int(input("Введите ваш ответ - "))
    actual_answer = num3 - num4
    print("Ваш ответ - ",user_answer)
    print("Правильный ответ - ",actual_answer)
    answers = (user_answer, actual_answer)
    return answers

def correct(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("Ответы совпали !!!")
    else:
        print("Овтеты НЕ совпали !!!")

def main():
    print("1) Сложение ")
    print("2) Вычитание ")
    choice = int(input("Выберите пункт меню: "))
    if choice == 1:
        user_answer, actual_answer = addition()
        correct(user_answer, actual_answer)
    elif choice == 2:
        user_answer, actual_answer = subtraction()
        correct(user_answer, actual_answer)
    else:
        print("Введите корректный номер !!!")

main()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 121 Работа со списком имен через меню

def add_name():
    name = input("Введите Имя: ")
    names.append(name)
    return names

def change_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
    select_num = int(input("Введите номер элемента для изменения: "))
    name = input("Введите новое Имя: ")
    names[select_num] = name
    return names

def del_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
    select_num = int(input("Введите номер элемента для удаления: "))
    del names[select_num]
    return names

def view_names():
    for x in names:
        print(x)
    print()

def main():
    again = "yes"
    while again == "yes":
        print("1) Добавить Имя")
        print("2) Изменить Имя")
        print("3) Удалить Имя")
        print("4) Просмотр Имён")
        print("5) Выход")
        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            names = add_name()
        elif choice == 2:
            names = change_name()
        elif choice == 3:
            names = del_name()
        elif choice == 4:
            names = view_names()
        elif choice == 5:
            again = "no"
        else:
            print("Введите правельный номер пункта меню !!!")
        
names = []
main()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 122 Работа c файлами .csv через меню

import csv

def add_to_file():
    file = open("Salaries.csv", "a")
    name = input("Введите имя сотруднкика: ")
    salary = int(input("Введите зарплату сотрудника: "))
    new_record = name + " - " + str(salary) + "руб" + "\n"
    file.write(str(new_record))
    file.close()

def view_all_record():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)

def main():
    again = True
    while again == True:
        print("1) Добавить в файл.")
        print("2) Просмотреть записи в файле.")
        print("3) Выход.")
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            add_to_file()
        elif choice == 2:
            view_all_record()
        elif choice == 3:
            again = False
        else:
            print("Введен некорректный пункт меню !!!")

main()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 123 Работа c файлами .csv, меню с возможностью удаления

import csv

def add_to_file():
    file = open("Salaries.csv", "a")
    name = input("Введите имя сотруднкика: ")
    salary = int(input("Введите зарплату сотрудника: "))
    new_record = name + " - " + str(salary) + "руб." + "\n"
    file.write(str(new_record))
    file.close()

def view_all_record():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)

def delete_record():
    file = open("Salaries.csv", "r")
    tmp = []
    x = 0
    for row in file:
        tmp.append(row)
    file.close()
    for row in tmp:
        print(x,row)
        x = x + 1
    choice_del = int(input("Введите номер строки для удаления: "))
    del tmp[choice_del]
    file = open("Salaries.csv", "w")
    for row in tmp:
        file.write(row)
    file.close()

def main():
    again = True
    while again == True:
        print("1) Добавить в файл.")
        print("2) Просмотреть записи в файле.")
        print("3) Удалить запись из файла")
        print("4) Выход.")
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            add_to_file()
        elif choice == 2:
            view_all_record()
        elif choice == 3:
            delete_record()
        elif choice == 4:
            again = False
        else:
            print("Введен некорректный пункт меню !!!")

main()
"""
# ---------------------------------------