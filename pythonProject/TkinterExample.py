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
    
    button1 = Button(text = "Click here", command = click)          -  создается кнопка для запуска подпрограммы click
    
    label.place(x = 50, y = 20, width = 100, height = 25)           -  задается расположение объекта в окне
    entry_box.delete(0, END)                                        -   удаляет содержимое отдельного эл-та или всего списка
    num = entry_box.get()                                           -   сохраняет содержимое поля ввода текста в переменную (не работает для областей вывода данных) 
    answer = output_txt["text"]                                     -   сохраняет содержимое области вывода в переменной (не работает для полей текстового ввода)
    output_txt["text"] = total                                      -   изменяет содержимое области вывода данных для отображеня значения переменной
    
    
    window.mainloop()                                               -   завершающая команда
    
    
    window.wm_iconbitmap("MyIcon.ico")                              -   изменение значка в заголовке окна
    window.configure(background = "light gree")                     -   изменяет цвет фона окна
    
    logo = PhotoImage(file = "logo.gif")                            -   выводим изображение в Label. Неизменяется во время выполнения программы 
    logoimage = Label(image = logo)
    logoimage.place(x = ,y = ,width = , height = )
    
    photo = PhotoImage(file = "logo.gif")                           -   выводим изображение в Label. Изменяется благодаря 3 строчке
    photobox = Label(window, image = photo)
    photobox.image = photo
    photobox.place(x,y,width,height)
    
    selectName = StringVar(window)                                  -   с переменной selectName связывается строка "Select Name", затем создается раскрывающийся список
    selectName.set("Select Name")                                       в котором отображается значения из переменной selectName и добавляются значения из списка namesList 
    namesList = OptionMenu(window, SelectName, "Petya", "Katya")
    nameList.place(x,y,width,height)
    
    
    def clicked ():                                                 -   при нажатии кнопки выполняется подпрограмма clicked(). Получаем значение из переменной selectName и создается сообщение
        sel = selectName.get()                                          Затем проверяется какой вариант выбран (Петя, Катя и тд) и отображается при помощи переменной photo
        mesg = "Hello " + sel
        mlabel["text"] = mesg
        if sel == "Petya":
            photo = PhotoImage(file = "Petya.gif")
            photobox.image = photo
        elif sel == "Katya":
            photo = PhotoImage(file = "Katya.gif")
            photobox.image = photo
        else:
            photo = PhotoImage(file = "Name.gif")
            photobox.image = photo            
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
"""
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
"""
# ---------------------------------------


# ---------------------------------------
"""
#128 Преобразование расстояния с использованием tkinter

from tkinter import *
import math

def Km_to_mil():
    rast = text_entry_rast.get()
    rast = int(rast)
    rast_to_mil = round(rast * 0.6214, 4)
    text_out_result["text"] = str(rast_to_mil) + " миль"

def Mil_to_km():
    rast = text_entry_rast.get()
    rast = int(rast)
    rast_to_km = round(rast * 1.6093, 4)
    text_out_result["text"] = str(rast_to_km) + " километров"

window = Tk()
window.title("Перевод расстояния")
window.geometry("600x300")

label_rast = Label(text = " Введите расстояние: ")
label_rast.place(x = 30,y = 30, width = 180)
label_rast["relief"] = "ridge"
label_rast["bg"] = "white"
label_rast["fg"] = "black"

label_info = Label(text = " 1 километр = 0,6214 мили \n" "1 миля = 1,6093 километра")
label_info.place(x = 30, y = 60, width = 180)
label_info["relief"] = "ridge"
label_info["bg"] = "white"
label_info["fg"] = "black"

text_entry_rast = Entry(text = 0)
text_entry_rast.place(x = 230,y = 31, width = 140, height = 20)
text_entry_rast.focus()
text_entry_rast["justify"] = "center"
text_entry_rast["fg"] = "black"

button_to_km = Button(text = "Перевести километры в мили", command = Km_to_mil)
button_to_km.place(x = 30,y = 120, width = 180, heigh = 22)
button_to_km["relief"] = "raised"
button_to_km["bg"] = "white"
button_to_km["fg"] = "black"

button_to_mil = Button(text = "Перевести мили в километры", command = Mil_to_km)
button_to_mil.place(x = 30,y = 150, width = 180, heigh = 22)
button_to_mil["relief"] = "raised"
button_to_mil["bg"] = "white"
button_to_mil["fg"] = "black"

text_out_result = Message(text = 0)
text_out_result.place(x = 230,y = 121, width = 140, height = 51)
text_out_result["justify"] = "center"
text_out_result["relief"] = "sunken"
text_out_result["fg"] = "black"
text_out_result["bg"] = "white"

window.mainloop()
"""
# ---------------------------------------


# ---------------------------------------
"""
#129-130 Список с целыми числами, с использованием tkinter. Сохранение в .csv

from tkinter import *
import csv

def Num_check():
    num = text_entry_num.get()
    if num.isdigit():
        text_out_list.insert(END, num)
        text_entry_num.delete(0,END)
        text_entry_num.focus()
    else:
        text_entry_num.delete(0,END)
        text_entry_num.focus()

def Save_to_csv():
    file = open("ListNumbers_130.csv", "w")
    elem = 0
    tmp_list = text_out_list.get(0, END)
    for i in tmp_list:
        new_record = tmp_list[elem] + "\n"
        file.write(str(new_record))
        elem = elem + 1
    file.close()

def Clear_List():
    text_out_list.delete(0,END)
    text_entry_num.focus()


window = Tk()
window.title("Проверка чисел")
window.geometry("600x400")

label_info = Label(text = " Введите число: ")
label_info.place(x = 30,y = 30, width = 180)
label_info["relief"] = "ridge"
label_info["bg"] = "white"
label_info["fg"] = "black"

text_entry_num = Entry(text = 0)
text_entry_num.place(x = 230,y = 31, width = 140, height = 20)
text_entry_num.focus()
text_entry_num["justify"] = "center"
text_entry_num["fg"] = "black"

button_num_check = Button(text = "Проверка, является ли \n число целым", command = Num_check )
button_num_check.place(x = 30,y = 90, width = 180, heigh = 35)
button_num_check["relief"] = "solid"
button_num_check["bg"] = "white"
button_num_check["fg"] = "black"

text_out_list = Listbox()
text_out_list.place(x = 230,y = 90, width = 140, height = 180)
text_out_list["bg"] = "white"
text_out_list["fg"] = "black"
text_out_list["justify"] = "center"
text_out_list["relief"] = "groove"

button_save_csv = Button(text = "Сохранить в .csv", command = Save_to_csv )
button_save_csv .place(x = 410,y = 200, width = 140, heigh = 22)
button_save_csv ["relief"] = "solid"
button_save_csv ["bg"] = "white"
button_save_csv ["fg"] = "black"

button_clear_list = Button(text = "ОЧИСТИТЬ СПИСОК", command = Clear_List )
button_clear_list.place(x = 410,y = 250, width = 140, heigh = 22)
button_clear_list["relief"] = "solid"
button_clear_list["bg"] = "white"
button_clear_list["fg"] = "black"

window.mainloop()
"""
# ---------------------------------------


# ---------------------------------------
"""
#131-132 Работа с .csv, с использованием tkinter, вывод списка

from tkinter import *
import csv

def Create_csv():
    file = open("Ages_131.csv", "w")
    file.close()

def Disp_csv():
    file = list(csv.reader(open("Ages_131.csv")))
    x = 0
    disp_list = []
    for row in file:
        disp_list.append(row)
    for i in disp_list:
        elem = disp_list[x]
        text_out_list.insert(END, elem)
        x = x + 1

def Clear_list():
    text_out_list.delete(0, END)
    text_entry_name.focus()

def Save_to_csv():
    file = open("Ages_131.csv", "a")
    name = text_entry_name.get()
    age = text_entry_age.get()
    new_record = "Имя - " + name + ". Возраст - " + age + "\n"
    file.write(str(new_record))
    file.close()
    text_entry_name.delete(0, END)
    text_entry_age.delete(0, END)
    text_entry_name.focus()

window = Tk()
window.title("Работа с CSV")
window.geometry("600x400")

label_name = Label(text = " Введите имя: ")
label_name.place(x = 30,y = 30, width = 120)
label_name["relief"] = "ridge"
label_name["bg"] = "white"
label_name["fg"] = "black"

text_entry_name = Entry(text = " ")
text_entry_name.place(x = 230,y = 30, width = 160, height = 20)
text_entry_name.focus()
text_entry_name["justify"] = "center"
text_entry_name["fg"] = "black"

label_age = Label(text = " Введите возраст: ")
label_age.place(x = 30,y = 60, width = 120)
label_age["relief"] = "ridge"
label_age["bg"] = "white"
label_age["fg"] = "black"

text_entry_age = Entry(text = 0)
text_entry_age.place(x = 230,y = 60, width = 160, height = 20)
text_entry_age.focus()
text_entry_age["justify"] = "center"
text_entry_age["fg"] = "black"

text_out_list = Listbox()
text_out_list.place(x = 230,y = 90, width = 200, height = 180)
text_out_list["bg"] = "white"
text_out_list["fg"] = "black"
text_out_list["justify"] = "center"
text_out_list["relief"] = "groove"

button_create_csv = Button(text = "Создать новый .csv файл", command = Create_csv )
button_create_csv.place(x = 30,y = 100, width = 180, heigh = 35)
button_create_csv["relief"] = "solid"
button_create_csv["bg"] = "white"
button_create_csv["fg"] = "black"

button_save_csv = Button(text = "Сохранить в .csv", command = Save_to_csv )
button_save_csv .place(x = 30,y = 150, width = 180, heigh = 35)
button_save_csv["relief"] = "solid"
button_save_csv["bg"] = "white"
button_save_csv["fg"] = "black"

button_disp_csv = Button(text = "Отобразить содержимое \n файла", command = Disp_csv )
button_disp_csv.place(x = 30,y = 200, width = 180, heigh = 35)
button_disp_csv["relief"] = "solid"
button_disp_csv["bg"] = "white"
button_disp_csv["fg"] = "black"

button_clear_list = Button(text = "Очистить список", command = Clear_list )
button_clear_list.place(x = 30,y = 250, width = 180, heigh = 22)
button_clear_list["relief"] = "solid"
button_clear_list["bg"] = "white"
button_clear_list["fg"] = "black"

window.mainloop()
"""
# ---------------------------------------

