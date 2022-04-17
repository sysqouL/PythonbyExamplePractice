#-------------------------------------------------
"""
"""

"""
    Задание 21.1:
    Создать функцию parse_command_output. Параметры функции:
    * template - имя файла, в котором находится шаблон TextFSM
      Например, templates/sh_ip_int_br.template
    * command_output - вывод соответствующей команды show (строка)
    Функция должна возвращать список:
    * первый элемент - это список с названиями столбцов
    * остальные элементы это списки, в котором находятся результаты обработки вывода
    Проверить работу функции на выводе команды sh ip int br с оборудования
    и шаблоне templates/sh_ip_int_br.template.
"""

import textfsm
from pprint import pprint

def parse_command_output(template, command_output):
    with open(template) as f:
        fsm = textfsm.TextFSM(f)                        # создаем объект в TextFSM
        header = fsm.header                             # имена переменных (столбцы)
        #print(header)
        result = fsm.ParseText(command_output)          # обрабатывем вывод и возвращаем список списков
        #print(result)
    return [header]+result


if __name__ == "__main__":
    temp = "templates/sh_ip_int_brief.template"             # "templates/sh_ip_int_brief_hua.template"
    with open("output/sh_ip_int_brief.txt") as show:           # "output/sh_ip_int_brief_hua.txt"
        output = show.read()
    result = parse_command_output(temp, output)
    print()
    pprint(result)
