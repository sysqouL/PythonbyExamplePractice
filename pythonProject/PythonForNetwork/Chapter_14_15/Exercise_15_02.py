#-------------------------------------------------
"""
"""

"""
    Задание 15.2
    Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
    имя файла, в котором находится вывод команды show ip int br
    Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
    * Interface
    * IP-Address
    * Status
    * Protocol
    Информация должна возвращаться в виде списка кортежей.
"""

import re
from pprint import pprint


def parse_sh_ip_int_br(showipintbrief):
    """
    :param showipintbrief: файл
    :return: result - список кортежей
    """
    regex = r"(\S+) +(\S+) +\w+ \w+ +(administratively down|up|down) +(up|down)"
    with open(showipintbrief) as f:
        # через for match in re.finditer(regex, f.read()):
        #       result.append(match.groups())
        result = [match.groups() for match in re.finditer(regex, f.read())]
    return result

if __name__ == "__main__":
    pprint(parse_sh_ip_int_br("sh_ip_int_brf.txt"))