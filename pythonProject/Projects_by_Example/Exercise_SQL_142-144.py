#-------------------------------------------------
"""
"""

"""
    Задание 142 - вывод информации из бд BookInfo по введенному месту рождения Автора
    Задание 143 - вывод информации из бд BookInfo по введённому году публикации
    Задание 144 - сохранение в файл по введенному Автору
"""

import sqlite3

def view_authors():
    cursor.execute("""SELECT Authors.Name, Authors.PlaceofBirth, Books.DatePublished 
    FROM Authors, Books WHERE Authors.Name = Books.Author""")
    #print("\n"+"-"*66+"\n")
    print()
    print("Список Авторов и дата публикаций произведений:")
    for x in cursor.fetchall():
        print(x)
    #print("\n"+"-"*66)

def search_placeb():
    enterplaceb = input("Введите место рождения: ")
    cursor.execute("""SELECT Books.Title, Books.DatePublished, Authors.Name
    FROM Books, Authors WHERE Authors.Name = Books.Author
    AND PlaceofBirth =?""",[enterplaceb])
    print()
    print("Согласно введенному месту рождения:")
    for x in cursor.fetchall():
        print(x)
    #print("\n"+"-"*66)

def search_datep():
    choicedatep = int(input("Введите год публикации: "))
    cursor.execute("""SELECT * FROM Books 
    WHERE DatePublished > ? ORDER BY DatePublished""", [choicedatep])
    print()
    print(f"Изданные после {choicedatep}:")
    for x in cursor.fetchall():
        print(x)
    #print("\n" + "-" * 66)

def search_authors():
    choiceauthor = input("Введите имя Автора: ")
    cursor.execute("""SELECT * FROM Books  
    WHERE Author =?""", [choiceauthor])
    with open("BooksList.txt", "w") as f:
        for x in cursor.fetchall():
            f.write(str(x[0]) + " - " + str(x[1]) + " - " + str(x[2]) + " - " + str(x[3]) + "\n")

def view_booklist():
    print()
    print("Автор и его произведения:")
    with open("BooksList.txt", "r") as i:
        for j in i:
            print(j.rstrip())

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

def main():
    Again = True
    while Again:
        print("\n"+"*"*30+" МЕНЮ "+"*"*30)
        print("1) Вывести список Авторов")
        print("2) Поиск по месту рождения")
        print("3) Поиск по году издания")
        print("4) Поиск по Автору и сохранение в файл BookList.txt")
        print("5) Отобразить список из BookList.txt")
        print("6) Выход")
        print("*" * 66 + "\n")
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            view_authors()
        elif choice == 2:
            search_placeb()
        elif choice == 3:
            search_datep()
        elif choice == 4:
            search_authors()
        elif choice == 5:
            view_booklist()
        elif choice == 6:
            Again = False
        else:
            print("Некорректный пункт меню")

main()
db.close()