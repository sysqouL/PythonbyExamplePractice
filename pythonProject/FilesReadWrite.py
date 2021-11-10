# ---------------------------------------
"""                                   """


"""
# Чтение и запись текстовых файлов
"""



"""
    file = open("Countries.txt", "w")  -  создается файл Countries. Если файл с таким именем уже есть, то он заменяется новым пустым. В него добавляются 3 строки с разрывами (\n). Затем файл закрывается.
    file.write("Italy\n")
    file.write("Germany\n")
    file.write("Spain\n")
    file.close()
    
    file = open("Countries.txt","r")  -  открывается файл в режиме чтения и выводится все содержимое файла
    print(file.read())
    
    file = open("Countries.txt", "a")  -  открывается файл в режиме присоединения, добавляется строка и файл закрывается. Если нету close() - изменения не будут сохранены
    file.write("France\n")
    file.close()
"""


# ---------------------------------------
"""
# 105 Создание файла с числами

file = open("Numbers.txt", "w")
file.write("15, ")
file.write("29, ")
file.write("3, ")
file.write("9, ")
file.write("55")
file.close()

"""
# ---------------------------------------


# ---------------------------------------
"""
# 106 Создание файла с именами

file = open("Names.txt", "w")
file.write("John\n")
file.write("Mike\n")
file.write("Bishop\n")
file.write("Ann\n")
file.write("Mari\n")
file.close()

"""
# ---------------------------------------


# ---------------------------------------
"""
# 107 Чтение из файла

file = open("Names.txt", "r")
print(file.read())
file.close()

"""
# ---------------------------------------


# ---------------------------------------
"""
# 108 Добавление в файл

file = open("Names.txt", "a")
NewName = input("Введите новое имя и добавить его в файл: ")
file.write(NewName + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 109 Меню

print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = int(input("Make a selection 1,2 or 3: "))
if selection == 1:
    subject = input("Введите название предмета для добавления в файл/перезаписи: ")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("Subject.txt", "w")
    file.write("SUBJECTS:")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
elif selection == 3:
    newsub = input("Введите название для добавления предмета в файл: ")
    file = open("Subject.txt", "a")
    file.write(newsub + '\n')
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
else:
    print("Неправельный выбор")
"""
# ---------------------------------------


# ---------------------------------------
"""
# 110 Сохранение с условием

file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
choice = input("Выберите имя из списка: ")
choice = choice + "\n"
for row in file:
    if row != choice:
        file = open("Names2.txt", "a")
        newrecord = row
        file.write(newrecord)
        file.close()
file.close()
"""
# ---------------------------------------