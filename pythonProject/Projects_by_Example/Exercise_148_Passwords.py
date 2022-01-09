# ---------------------------------------
""""""

"""
    Задание 148. Учебные проекты. Пароли
"""


import csv

def get_data():
    # функция для взятие данных из файла, тк файл .csv данные переносим в список
    file = list(csv.reader(open("Password.csv")))
    tmp = []
    for x in file:
        tmp.append(x)
    return tmp

def create_userID(tmp):
    # функция создания нового UserID,
    # входные данные - список tmp
    # возвращаем UserID
    AgainID = True
    while AgainID:
        newUserID = input("Введите новый UserID: ")
        newUserID.lower()
        inList = False
        row = 0
        # для каждого элемента в списке, если введ UserID есть в 1 строке 1 эл-та списка
        # проверяем следующую строку
        for y in tmp:
            if newUserID in tmp[row][0]:
                print(f"Введённый UserID-{newUserID}, есть в списке")
                inList = True
            row = row + 1
        if inList == False:
             AgainID = False
    return newUserID

def create_password():
    # функция для создания пароля, согласно заданным критериям начисляются очки
    spec_sym_list = ["!", "$", "%", "<", ">", "*", "@","&"]
    numb_list = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Again = True
    password = input("Введите пароль: ")
    while Again:
        score = 0
        Upper = False
        Lower = False
        Spec = False
        Numb = False
        lenght = len(password)
        if lenght >= 8:
            score = score + 1
        for x in password:
            if x.islower():
                Lower = True
            if x.isupper():
                Upper = True
            if x in spec_sym_list:
                Spec = True
            if x in numb_list:
                Numb = True
        if Lower == True:
            score = score + 1
        if Upper == True:
            score = score + 1
        if Spec == True:
            score = score + 1
        if Numb == True:
            score = score + 1
        if 1 <= score <= 2:
            print("Пароль слишком короткий. Попробуйте другой пароль")
        if 3 <= score <= 4:
            print(f"Пароль набрал - {score} балов, но его можно усилить")
            imp_pas = input("Вы хотите ввести пароль лучше ?(yes/no): ")
            imp_pas.lower()
            if imp_pas == "no":
                Again = False
            else:
                password = input("Введите усиленный пароль: ")
        if score >= 5:
            print("Вы ввели сильный пароль")
            Again = False
    return password

def find_user(tmp):
    # функция поиска по UserID
    Again = True
    newUserID = ""
    while Again:
        searchID = input("Введите UserID: ")
        searchID.lower()
        inList = 0
        row = 0
        for y in tmp:
            if searchID in tmp[row][0]:
                inList = True
            row = row + 1
        if inList == True:
            newUserID = searchID
            Again = False
        else:
            print(f"Данного {searchID} ID нет в списке")
    return newUserID

def change_password(newUserID,tmp):
    # функция изменения пароля
    if newUserID != "":
        password = create_password()
        ID = newUserID.index(newUserID)
        tmp[ID][1] = password
        file = open("Password.csv", "w")
        x = 0
        for row in tmp:
            newrecord = tmp[x][0] + ', ' + tmp[x][1] + '\n'
            file.write(newrecord)
            x = x + 1
        file.close()

def display_all_userID():
    # функция вывода userID
    tmp = get_data()
    x = 0
    for row in tmp:
        print(tmp[x][0])
        x = x + 1

def main():
    tmp = get_data()
    Again = True
    while Again:
        print()
        print("1) Создать новый User ID")
        print("2) Изменить пароль")
        print("3) Отобразить все User ID")
        print("4) Выход")
        print()
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            newUserID = create_userID(tmp)
            password = create_password()
            file = open("Password.csv", "a")
            newrecord = newUserID + ", " + password + "\n"
            file.write(str(newrecord))
            file.close()
        elif choice == 2:
            newUserID = find_user(tmp)
            change_password(newUserID, tmp)
        elif choice == 3:
            display_all_userID()
        elif choice == 4:
            Again = False
        else:
            print("Вы ввели неверный пункт меню")
main()

