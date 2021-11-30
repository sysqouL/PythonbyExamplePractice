# ---------------------------------------
"""                                   """


"""
# Работа с библиотекой Tkinter
"""

"""
    from tkinter export  -  импорт библиотеки
    
    window = Tk()                           -   создание окна
    window.title("Загаловок окна")
    window.geometry("450x100")              -   размер окна
    label = Label(text = "Введите текст: ") -   текстовый элемент на экран
    entry_box = Entry (text = " ")          -   создание пустого текстового поля для ввода/вывода данных
    output_box = Message(text = " ")        -   область для вывода данных
    
    output_box ["bg"] = "red"               -   цвет фона для объекта
    output_box ["fg"] = "black"             -   цвет шрифта для объекта 
    output_box ["relief"] = "sunken"        -   стиль объемного обрамления элемента: flat - отсутствие рамки; 
                                                raised - эффект рельефа; sunken - углубление; groove - углебление рамки;
                                                ridge - рельефная рамка;
                                                
    list_box = Listbox()                    -   создает раскрывающийся список, содержащий только строки
    entry_box ["justify"] = "center"        -   режим выравнивания текста в поле (не работает для областей вывода данных)
    
    button1 = Button(text = "Click here", command = click)  -  создается кнопка для запуска подпрограммы click
    
    label.place(x = 50, y = 20, width = 100, height = 25)  -  задается расположение объекта в окне
    entry_box.delete(0, END)                -   удаляет содержимое отдельного эл-та или всего списка
    num = entry_box.get()                   -   сохраняет содержимое поля ввода текста в переменную (не работает для областей вывода данных) 
    answer = output_txt["text"]             -   сохраняет содержимое области вывода в переменной (не работает для полей текстового ввода)
    output_txt["text"] = total              -   изменяет содержимое области вывода данных для отображеня значения переменной
    
    window.mainloop()                       -   завершающая команда
"""


# ---------------------------------------

# 124 Ввод/вывод имени с визуальным изменением
"""
from tkinter import *

def Click():
    name = textbox.get()
    message = str("Привет " + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "red"
    textbox2["text"] = message

window = Tk()
window.title("Окно задания 124")
window.geometry("700x500")

label1 = Label(text = "Введите ваше Имя: ")
label1.place(x = 50,y = 50)

textbox = Entry(text = " ")
textbox.place(x = 170,y = 45, width = 120, height = 30)
textbox["justify"] = "center"

button1 = Button(text = "Нажмите сюда", command = Click)
button1.place(x = 300,y = 45, width = 120, heigh = 30)

textbox2 = Message(text = " ")
textbox2.place(x = 170,y = 80, width = 120, height = 30)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()
"""
# ---------------------------------------


# ---------------------------------------

#125 моделирование броска шестигранного кубика
"""
from tkinter import *
import random

def Click_random():
    num = random.randint(1,6)
    textbox1["text"] = num

window = Tk()
window.title("БРОСОК КУБИКА")
window.geometry("1000x700")

label1 = Label(text = "Нажмите кнопку что бы бросить кубик")
label1.place(x = 50,y = 50)

button1 = Button(text = "БРОСАЕМ !!!", command = Click_random)
button1.place(x = 300,y = 45, width = 120, heigh = 30)

label2 = Label(text = "Вам выпало :")
label2.place(x = 50,y = 85)

textbox1 = Message(text = " ")
textbox1.place(x = 300,y = 80, width = 120, height = 30)
textbox1["bg"] = "white"
textbox1["fg"] = "black"

window.mainloop()
"""
# ---------------------------------------

# ---------------------------------------
"""
#126 накопление/обнуление суммы

from tkinter import *

def Sum():                                                          # подпрограмма сложения введенных чисел
    num = textbox_enter.get()                                       # сохраняем в переменной данные, введенные в поле ввода
    num = int(num)                                                  # меняем тип для сложения
    answer = textbox_out["text"]                                    # присваиваем переменной
    answer = int(answer)                                            # меняем тип для сложения
    result = num + answer
    textbox_out["text"] = result                                    # в область вывода сохраняем сумму чисел

def Zero():                                                         # подпрограмма обнуления
    textbox_out["text"] = 0                                         # в поле вывода сохраняем 0
    textbox_enter.delete(0, END)                                    # удаляем содержимое

result = 0
num = 0

window = Tk()
window.title("Накопление суммы")
window.geometry("800x800")

label1 = Label(text = "Введите число: ")
label1.place(x = 50,y = 50)

textbox_enter = Entry(text = 0)
textbox_enter.place(x = 180,y = 45, width = 120, height = 30)
textbox_enter["justify"] = "center"
textbox_enter["relief"] = "sunken"

button_sum = Button(text = "Накопление", command = Sum)
button_sum.place(x = 310,y = 45, width = 120, heigh = 30)

label2 = Label(text = "Накопленная сумма: ")
label2.place(x = 50,y = 85)

textbox_out = Message(text = 0)
textbox_out.place(x = 180,y = 80, width = 120, height = 30)
textbox_out["bg"] = "white"
textbox_out["fg"] = "black"
textbox_out["relief"] = "sunken"

button_zero = Button(text = "Обнуление", command = Zero)
button_zero.place(x = 310,y = 80, width = 120, heigh = 30)

window.mainloop()
"""
# ---------------------------------------

# ---------------------------------------

#127 Список имен с использованием tkinter

from tkinter import *

def Add_to_List():                                                  # подпрограмма добавления в список
    name = text_entry_name.get()
    text_out_list.insert(END, name)                                 # используем insert для вставки элемента в заданную позицию
    text_entry_name.delete(0, END)
    text_entry_name.focus()

def Clear_List():                                                   # подпрограмма очистки списка
    text_out_list.delete(0, END)
    text_entry_name.focus()

window = Tk()
window.title("Работа со списком Имен")
window.geometry("600x300")

label1 = Label(text = "ВВЕДИТЕ ИМЯ - ")
label1.place(x = 50,y = 50)
label1["relief"] = "ridge"

text_entry_name = Entry(text = " ")
text_entry_name.place(x = 155,y = 50, width = 120, height = 22)
text_entry_name.focus()
text_entry_name["justify"] = "center"
text_entry_name["relief"] = "groove"

button_add_to_list = Button(text = "ДОБАВИТЬ В КОНЕЦ СПИСКА", command = Add_to_List)
button_add_to_list.place(x = 310,y = 50, width = 240, heigh = 22)
button_add_to_list["relief"] = "raised"
button_add_to_list["bg"] = "white"
button_add_to_list["fg"] = "black"

label2 = Label(text = "СПИСОК - ")
label2.place(x = 50,y = 100)
label2["relief"] = "ridge"

text_out_list = Listbox()
text_out_list.place(x = 155,y = 100, width = 120, height = 180)
text_out_list["bg"] = "white"
text_out_list["fg"] = "black"
text_out_list["justify"] = "center"
text_out_list["relief"] = "groove"

button_clear_list = Button(text = "ОЧИСТИТЬ СПИСОК", command = Clear_List )
button_clear_list.place(x = 410,y = 250, width = 140, heigh = 22)
button_clear_list["relief"] = "raised"
button_clear_list["bg"] = "white"
button_clear_list["fg"] = "black"

window.mainloop()