# ---------------------------------------
# Работа со строками
"""
"""


"""
# if строка.isupper():   -   если строка из букв верхнего регистра то выводится сообщение
    print("Uppercase")       строка.islower()  -  аналог isupper только для нижнего регистра
  else:
    print("Not upper")

    print(символ, end="*")  -  после каждого символа выводится символ *
"""


# ---------------------------------------
"""
# 80 Имя Фамилия

name = input("Введите Имя: ")
print("Имя -", name,"- Длинна имени -", len(name))
print()
surname =input("Введите Фамилию: ")
print("Фамилия -", surname,"- Длинна фамилии -", len(surname))
namesur = name + " " + surname
print()
print(namesur,"- Полная длинна -", len(namesur))
"""
# ---------------------------------------


# ---------------------------------------
"""
# 81 Школьный предмет

subject = input("Введите любимый школьный предмет - ")
for simvol in subject:
    print(simvol,end="-")
"""
# ---------------------------------------


# ---------------------------------------
"""
# 82 Позиции в строках

stih = input("Введите строку из стихотворения: ")
print()
start = int(input("Введите начальную позицию: "))
end = int(input("Введите конечную позицую: "))
print(stih[start:end])
"""
# ---------------------------------------


# ---------------------------------------
"""
# 83 Верхний регистр

word = input("Введите слово в верхнем регистре: ")
tryagain = False
while tryagain == False:
    if word.isupper():
        print()
        print("Слово введенно корректно")
        tryagain = True
    else:
        print()
        print("Слово введенно некоректно. Повторите попытку")
        word = input("Введите слово в верхнем регистре: ")
"""
# ---------------------------------------


# ---------------------------------------
"""
# 84 Почтовый индекс

pocht_index = input("Введите свой почтовый индекс: ")
print("Индекс -", pocht_index)
start = pocht_index[0:2]
print(start.upper())
"""
# ---------------------------------------


# ---------------------------------------
"""
# 85 Гласные буквы в тексте

vved_text = input("Введите текст - ")
count = 0
vved_text = vved_text.lower()
for i in vved_text:
    if i == "а" or i == "е" or i == "и" or i == "о" or i == "у" or i == "ы" or i == "э" or i == "ю" or i == "я" or i == "ё":
        count = count + 1
print("Гласных букв в тексте - ",count)
"""
# ---------------------------------------


# ---------------------------------------
"""
# 86 Пароли

password = input("Введите пароль: ")
passanother = input("Введите пароль еще раз: ")
if password == passanother:
    print("Пароли совпадают")
elif password.lower() == passanother.lower():
    print("Различия в регистре")
else:
    print("Некорректно")
"""
# ---------------------------------------


# ---------------------------------------
"""
# 87 Вывод в обратном порядке

word = input("Введите слово - ")
count = 1
lenght = len(word)
for i in word:
    pos = lenght - count
    letter = word[pos]
    print(letter)
    count = count + 1
"""
# ---------------------------------------