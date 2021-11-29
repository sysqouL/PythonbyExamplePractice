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
    answer = output_txt["text"]             -   сохраняет содержимое области ввода в переменной (не работает для полей текстового ввода)
    output_txt["text"] = total              -   изменяет содержимое области вывода данных для отображеня значения переменной
    
    window.mainloop()                       -   завершающая команда
"""


# ---------------------------------------

# 124 Ввод/вывод имени с визуальным изменением

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

label1 = Label(text = "Ввидите ваше Имя: ")
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