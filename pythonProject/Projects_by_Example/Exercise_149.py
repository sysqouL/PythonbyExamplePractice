# ---------------------------------------
""""""

"""
    Задание 149. Учебные проекты. Таблица умножения с использованием Tkinter
"""


from tkinter import *

def view_table():
    num = box_number.get()
    num = int(num)
    count = 1
    for i in range(1,num + 1):
        result = i * num
        list_numbers.insert(END,(i, "x", num, "=", result))
        count = count + 1
        box_number.delete(0, END)
        box_number.focus()

def clear_table():
   list_numbers.delete(0, END)
   box_number.delete(0, END)
   box_number.focus()

window = Tk()
window.title(" Таблица Умножения ")
window.geometry("500x300")

label_number = Label(text = "Введите число: ")
label_number.place(x = 20, y = 20, width = 100, height = 25)
label_number["relief"] = "ridge"

box_number = Entry(text = 0)
box_number.place(x = 130, y = 20, width = 100, height = 25)
box_number.focus()

button_view = Button(text = " Вывести таблицу умножения ", command = view_table)
button_view.place(x = 250, y = 20, width = 180, height = 25)


list_numbers = Listbox()
list_numbers.place(x = 130, y = 50, width = 100, height = 200)

button_clear_list = Button(text = " Очистить таблицу ", command = clear_table)
button_clear_list.place(x = 250, y = 50, width = 180, height = 25)

window.mainloop()