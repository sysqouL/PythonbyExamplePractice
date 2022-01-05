#-------------------------------------------------
"""
"""

"""
    Задание 9.4 - создать функцию convert_cfg_to_dict, которая обрабатывает конф файл
    коммутатора и возвращает словарь:
    * все команды верхнего уровня должны быть ключами, подкоманды должны быть 
    в значении у соответсвующего ключа, в виде списка
    * игнорировать строки начин с ! и в которой содержаться слова из списка ignore
"""

ignore = ["duplex", "alias", "configuration"]

def ignore_command(command, ignore):
    """
    функция проверяет содержится ли в команде слово из списка ignore
    :param command: строка - команда которую нужно проверить
    :param ignore: список слов
    :return: True - если содержится слово из ignore, False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_cfg_to_dict(config_filename):
 config_dict = {}
 with open("config_sw1.txt") as f:
    for line in f:
        line = line.rstrip()
        # если строка нач не с ! и не содержит слово из ignore
        if line and not (line.startswith("!") or ignore_command(line, ignore)):
            # если первый символ с строке буква,цифра
            if line[0].isalnum():
                global_cfg = line
                # заносим строки глоб конфиг в ключи словаря
                config_dict[global_cfg] = []
            else:
                # заносим строки в элементы убирая пробелы с помощью .strip()
                config_dict[global_cfg].append(line.strip())
 return config_dict



