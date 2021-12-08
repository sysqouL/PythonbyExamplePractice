# ---------------------------------------
"""
#   Задание 146. Учебные проекты. Код сдвига
"""


""" 
    Каждая буква заменяется другой буквой, полученной сдвигом вперед по алфавиту на заданную величину. 
"""

alfavit = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
           "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           " ",",",".","?","!","-",":",";","_"]

def input_data():
    word = input("Введите сообщение: ")
    num = int(input("Введите номер для сдвига (1-61):"))
    if num > 61 or num == 0:
        while num > 61 or num == 0:
            print("Вы ввели некорректный номер для сдвига !!!")
    data = (word,num)
    return data

def code(word,num):
    new_word = ""
    for i in word:
        x = alfavit.index(i)                                # получаем индексы символов в ведденом слове
        x = x + num                                         # получаем индексы символов с учетом сдвига
        if x > 60:
            x = x - 61
        char = alfavit[x]                                   # получаем закодированные символы
        new_word = new_word + char                          # получаем закодированное слово
    print("Закодировано в -",new_word)
    print()

def decode(word,num):
    true_word = ""
    for i in word:
        x = alfavit.index(i)
        x = x - num
        if x < 0:
            x = x + 61
        char = alfavit[x]
        true_word = true_word + char
    print("Декадировано в -",true_word)
    print()

def main():
    Again = True
    while Again == True:
        print("1) Закодировать сообщение")
        print("2) Декодировать сообщение")
        print("3) Закрыть программу")
        print()
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            word,num = input_data()
            code(word,num)
        elif choice == 2:
            word,num = input_data()
            decode(word,num)
        elif choice == 3:
            Again = False
        else:
            print("Вы ввели неверный пункт меню")

main()