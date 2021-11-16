# ---------------------------------------
"""                                   """


"""
# Чтение и запись файлов .csv
"""


"""
    import csv  -  импорт библиотеки CSV для использования
    
    file = open("Example.txt", "w")  -  создается файл Example. Если файл с таким именем уже есть, то он заменяется новым пустым. Добавляется новая запись. (Если вместо w - x, при совпадении имен будет фатальная ошибка)
    newRecord = "Mitch, 34, Michigan\n"
    file.write(str(newrecord))
    file.close() 
    
    file = open("Example.txt","r")  -  открывается файл в режиме чтения и последовательно выводится все содержимое файла
    for row in file:
        print(row)
    
    file = open("Example.txt", "a")  -  открывается файл в режиме присоединения, добавляются строки и файл закрывается. Если нету close() - изменения не будут сохранены
    name = input("Enter name: ")
    age = input("Enter age: ")
    newRecord = name + ", " + age + "\n"
    file.close()
    
    import csv
    file = list(csv.reader(open("Example.txt")))  -  запись исходного файла .csv в список для последующего его изменения
    tmp = []
    for row in file:
        tmp.append(row)

"""


# ---------------------------------------
# 111 Создание файла csv- список книг
"""
import csv

file = open("Books.csv", "w")
newRecord = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(newRecord))
newRecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newRecord))
newRecord = "The Great Gatsby, F.Scott Fitzgerald, 1922\n"
file.write(str(newRecord))
newRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newRecord))
newRecord = "Pride and Prejudice, Jan Austen, 1813\n"
file.write(str(newRecord))
file.close()
"""
# ---------------------------------------


# ---------------------------------------
# 112 Добавление произвольной записи в Books.csv
"""
import csv

file = open("Books.csv", "a")
title = input("Введите название книги на английском: ")
author = input("Введите автора на английском: ")
year = input("Введите год выпуска: ")
newRecord = title + ", " + author + ", " + year + "\n"
file.write(str(newRecord))
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()
"""
# ---------------------------------------


# ---------------------------------------
# 113 Взаимодействие с Books.csv - поиск по автору, добавление по параметрам
"""
import csv

num = int(input("Сколько книг вы хотите добавить в файл: "))
file = open("Books.csv", "a")
for x in range(0, num):
    title = input("Введите название книги на английском: ")
    author = input("Введите автора на английском: ")
    year = input("Введите год выпуска: ")
    newRecord = title + ", " + author + ", " + year + "\n"
    file.write(str(newRecord))
file.close()

search_author = input("Введите имя автора для поиска: ")

file = open("Books.csv", "r")
count = 0
for row in file:
    if search_author in str(row):
        print("\n","Результат поиска:",row)
        count = count + 1
if count == 0:
    print("Данного автора нету в списке")
file.close()
"""
# ---------------------------------------


# ---------------------------------------
# 114 Взаимодействие с Books.csv - поиск по интервалу выпуска
"""
import csv

start = int(input("Введите начальный интервал года выпуска: "))
end = int(input("Введите конечный интервал года выпуска: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
        x = x + 1
"""
# ---------------------------------------


# ---------------------------------------
# 115 Взаимодействие с Books.csv - вывод количества строк
"""
import csv

file = open("Books.csv", "r")
x = 0
for row in file:
    display = "Row-" + str(x) + ": " + row
    print(display)
    x = x + 1
"""
# ---------------------------------------


# ---------------------------------------
# 116 Взаимодействие с Books.csv - импорт в список, удаление, изменение элементов. Запись изменений в файл
"""
import csv

file = list(csv.reader(open("Books.csv")))
BookList = []
for row in file:
    BookList.append(row)

x = 0
for row in BookList:
    print("Строка", x, "-", BookList[x])
    x = x + 1
choice_delete = int(input("Введите номер строки для удаления: "))
del BookList[choice_delete]

alternative = int(input("Введите номер строки для изменения: "))
x = 0
for row in BookList[alternative]:
    display = x, BookList[alternative][x]
    print(display)
    x = x + 1

part = int(input("Выберите часть для изменения (0 - Название,1 - Автор,2 - Год): "))
newdata = input("Введите новое значение: ")
BookList[alternative][part] = newdata
print("Измененная строка - ",BookList[alternative])

file = open("Books.csv", "w")
x = 0 
for row in BookList:
    new_record = BookList[x][0] + ", " + BookList[x][1] + ", " + BookList[x][2] + "\n"
    file.write(new_record)
    x = x + 1
file.close()
"""
# ---------------------------------------


# ---------------------------------------
# 117 Математическая игра - отвечайте правильно и зарабатывайте очки
"""
import csv
import random, math

score = 0
name = input("Игрок. Как вас зовут ? ")
q1_num1 = random.randint(0, 250)
q1_num2 = random.randint(0, 250)
question1 = str(q1_num1) + " + " + str(q1_num2) + " = "
answer1 = int(input(question1))
realanswer1 = q1_num1 + q1_num2
if answer1 == realanswer1:
    score = score + 1

q2_num1 = random.randint(30, 300)
q2_num2 = random.randint(10, 100)
question2 = str(q2_num1) + " / " + str(q2_num2) + " = "
answer2 = float(input(question2))
realanswer2 = q2_num1 / q2_num2
result2 = round(realanswer2, 4)
if answer2 == result2:
    score = score + 1

file = open("QuizScore.csv", "a")
new_record1 = "Имя: " + name + ", " + "Вопрос №1: " + question1 + ", " + "Ответ на первый вопрос: " + str(answer1) + ", " + "Количество очков: " + str(score) + "\n"
new_record2 = "Имя: " + name + ", " + "Вопрос №2: " + question2 + ", " + "Ответ на второй вопрос: " + str(answer2) + ", " + "Количество очков: " + str(score) + "\n"
file.write(str(new_record1))
file.write(str(new_record2))
file.close()
"""
# ---------------------------------------

