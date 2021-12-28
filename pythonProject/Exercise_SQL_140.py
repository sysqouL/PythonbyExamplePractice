#-------------------------------------------------
"""
"""

"""
    Задание 140 - дополнить 139 меню - просмотр, добавление, поиск по имени, удаление, выход
"""

import sqlite3

def view_phonebook():
    cursor.execute("SELECT * FROM PhoneBook")
    print()
    for x in cursor.fetchall():
        print(x)

def add_to_phonebook():
    new_id = int(input("Введите ID: "))
    new_firstname = input("Введите Имя: ")
    new_surname = input("Введите Фамилию: ")
    new_phonenumber = int(input("Введите Тел. Номер: "))
    cursor.execute("""INSERT INTO PhoneBook (id, FirstName, Surname, PhoneNumber)
    VALUES(?, ?, ?, ?)""", (new_id, new_firstname, new_surname, new_phonenumber))
    db.commit()

def search_in_phonebook():
    choice_name = input("Введите Имя: ")
    cursor.execute("""SELECT * FROM PhoneBook WHERE FirstName = ?""", [choice_name])
    print()
    for x in cursor.fetchall():
        print(x)

def delete_record():
    delete_id = int(input("Введите ID для удаления: "))
    cursor.execute("DELETE FROM PhoneBook WHERE id =?", [delete_id])
    cursor.execute("SELECT * FROM PhoneBook")
    print()
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

def main():
    Again = True
    while Again:
        print()
        print("---- Меню ----")
        print()
        print("1) Просмотреть телефонную книгу")
        print("2) Добавить запись в телефонную книгу")
        print("3) Поиск в телефонной книге по имени")
        print("4) Удалить запись из телефонной книги")
        print("5) Завершить работу")
        print()
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            view_phonebook()
        elif choice == 2:
            add_to_phonebook()
        elif choice == 3:
            search_in_phonebook()
        elif choice == 4:
            delete_record()
        elif choice == 5:
            Again = False
        else:
            print("Введен некорректный пункт меню !!!")

main()
db.close()