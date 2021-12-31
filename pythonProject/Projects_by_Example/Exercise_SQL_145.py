#-------------------------------------------------
"""
"""

"""
    Задание 145 - графическое меню tkinter для заполнения БД TestScores
"""

import sqlite3
from tkinter import *

def addtoList():
    newname = studentname.get()
    newgrade = studentgrade.get()
    cursor.execute(""" INSERT INTO Scores (name, score)
    VALUES(?, ?)""", (newname, newgrade))
    db.commit()
    studentname.delete(0, END)
    studentgrade.delete(0, END)
    studentname.focus()

def clearList():
    studentname.delete(0, END)
    studentgrade.delete(0, END)
    studentname.focus()

with sqlite3.connect("TestScore.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Scores(
    ID integer PRIMARY KEY,
    Name text,
    Score integer); """)

window = Tk()
window.title("Балы за Тест")
window.geometry("450x200")

label1 = Label(text = "Введите имя студента: ")
label1.place(x = 30, y = 35)
studentname = Entry(text = "")
studentname.place(x = 160, y = 35, width = 200, height = 25)
studentname.focus()

label2 = Label(text = "Введите оценку: ")
label2.place(x = 30, y = 80)
studentgrade = Entry(text = "")
studentgrade.place(x = 160, y = 80, width = 200, height = 25)
studentgrade.focus()

addbutton = Button(text = "Добавить", command = addtoList)
addbutton.place(x = 160, y = 120, width = 75, height = 25)
clearbutton = Button(text = "Очистить", command = clearList)
clearbutton.place(x = 260, y = 120, width = 75, height = 25)

window.mainloop()
db.close()