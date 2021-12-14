# ---------------------------------------
"""
#   Задание 147. Учебные проекты. Mastermind
"""

"""
    Компьютер генерирует комбинацию из 4 цветов. Пользователь должен угадать цвета и позиции.
"""

import random


def generation_col():                                                                               # подпрограмма генерации случайного выбора цветов
    col1 = random.choice(col_list)
    col2 = random.choice(col_list)
    col3 = random.choice(col_list)
    col4 = random.choice(col_list)
    data = (col1,col2,col3,col4)
    return data

def the_game(col1,col2,col3,col4):
    col_text = ",".join(col_list)                                                                   # для добавления списка в input
    print()
    print("Вам нужно четыре раза выбрать правельный цвет и угадать его позицию")
    Again = True
    while Again == True:
        choice1 = input("1 Выбор. Выберете один цвет из списка ({}): ".format(col_text))
        choice1 = choice1.lower()                                                                   # для учёта регистра
        if choice1 not in col_list:
            print("Выбор некорректен")
        else:
            Again = False
    Again = True
    while Again == True:
        choice2 = input("2 Выбор. Выберете один цвет из списка ({}): ".format(col_text))
        choice2 = choice2.lower()
        if choice2 not in col_list:
            print("Выбор некорректен")
        else:
            Again = False
    Again = True
    while Again == True:
        choice3 = input("3 Выбор. Выберете один цвет из списка ({}): ".format(col_text))
        choice3 = choice3.lower()
        if choice3 not in col_list:
            print("Выбор некорректен")
        else:
            Again = False
    Again = True
    while Again == True:
        choice4 = input("4 Выбор. Выберете один цвет из списка ({}): ".format(col_text))
        choice4 = choice4.lower()
        if choice4 not in col_list:
            print("Выбор некорректен")
        else:
            Again = False
    true_place = 0                                                                                  # правельная позиция
    wrong_place = 0                                                                                 # неправельная позиция
    if col1 == choice1:
        true_place = true_place + 1
    elif col1 == choice2 or col1 == choice3 or col1 == choice4:
        wrong_place = wrong_place + 1
    if col2 == choice2:
        true_place = true_place + 1
    elif col2 == choice1 or col2 == choice3 or col2 == choice4:
        wrong_place = wrong_place + 1
    if col3 == choice3:
        true_place = true_place + 1
    elif col3 == choice1 or col3 == choice2 or col3 == choice4:
        wrong_place = wrong_place + 1
    if col4 == choice4:
        true_place = true_place + 1
    elif col4 == choice1 or col4 == choice2 or col4 == choice3:
        wrong_place = wrong_place + 1
    print("*"*60)
    print("Правельный цвет в правельной позиции: ",true_place)
    print("Правельный цвет в неправельной позиции: ",wrong_place)
    data = (true_place,wrong_place)
    return data

def main():
    (col1,col2,col3,col4) = generation_col()                                                        # получаем переменные из подпрограммы generation_col()
    attempt = 0                                                                                     # количество попыток
    play = True
    while play == True:
        (true_place,wrong_place) = the_game(col1,col2,col3,col4)                                    # получаем правельные/неправельные позиции из the_game() в которую передали переменные из generation_col()
        attempt = attempt + 1
        if true_place == 4:
            play = False
    print("*" * 60)
    print("Игра завершена. Вы угадали")
    print("Количество попыток = ",attempt)


col_list = ["красный","жёлтый","зелёный","синий","белый","оранжевый","чёрный"]
main()
