#-------------------------------------------------
"""
"""

"""
    Задание 21.3
    Создать функцию parse_command_dynamic.
    Параметры функции:
    * command_output - вывод команды (строка)
    * attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
     * 'Command': команда
     * 'Vendor': вендор
    * index_file - имя файла, где хранится соответствие между командами и шаблонами.
      Значение по умолчанию - "index"
    * templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"
    Функция должна возвращать список словарей с результатами обработки
    вывода команды (как в задании 21.1a):
    * ключи - имена переменных в шаблоне TextFSM
    * значения - части вывода, которые соответствуют переменным
    Проверить работу функции на примере вывода команды sh ip int br.
"""

import textfsm
from textfsm import clitable
from pprint import pprint

def parse_command_dynamic(
    command_output, attributes_dict, index_file="index", template_path="templates"
):
    """
    Сначала надо инициализировать класс, передав ему имя файла, в котором хранится соответствие
    между шаблонами и командами, и указать имя каталога, в котором хранятся шаблоны:
    """
    cli_table = clitable.CliTable(index_file, template_path)
    # Методу ParseCmd надо передать вывод команды и словарь с параметрами
    cli_table.ParseCmd(command_output, attributes_dict)
    return [dict(zip(cli_table.header, row)) for row in cli_table]


if __name__ == "__main__":
    """
    Надо указать, какая команда передается, и указать дополнительные атрибуты, 
    которые помогут идентифицировать шаблон. Для этого нужно создать словарь, 
    в котором ключи - имена столбцов, которые определены в файле index
    """
    attributes = {"Command": "show ip int brief", "Vendor": "cisco_ios"}
    # ("output/sh_ip_int_brief_hua.txt"), и поменять файл в index
    with open("output/sh_ip_int_brief.txt") as f:
        command_output = f.read()
    result = parse_command_dynamic(command_output, attributes)
    pprint(result, width=100)