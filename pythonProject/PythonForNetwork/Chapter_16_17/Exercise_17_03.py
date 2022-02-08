#-------------------------------------------------
"""
"""

"""
    Задание 17.3
    Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
    вывод команды show cdp neighbors.
    Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
    Функция должна возвращать словарь, который описывает соединения между устройствами.
    Например, если как аргумент был передан такой вывод:
    R4>show cdp neighbors
    Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
    R5           Fa 0/1          122           R S I           2811       Fa 0/1
    R6           Fa 0/2          143           R S I           2811       Fa 0/0
    Функция должна вернуть такой словарь:
    {'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
            'Fa 0/2': {'R6': 'Fa 0/0'}}}
    Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
    Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
from pprint import pprint
import re


def parse_sh_cdp_neighbors(command_output):
    regex = re.compile(
        r"(?P<dev_ID>\w+)  +(?P<local_intf>\S+ \S+)"
        r"  +\d+  +[R S I ]+  +\S+ +(?P<port_ID>\S+ \S+)"
    )
    connect_dict = {}
    local_dev = re.search(r"(\S+)[>#]", command_output).group(1)
    connect_dict[local_dev] = {}
    for match in regex.finditer(command_output):
        dev_ID, local_intf, port_ID = match.group("dev_ID", "local_intf", "port_ID")
        connect_dict[local_dev][local_intf] = {port_ID: dev_ID}
    return connect_dict


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        pprint(parse_sh_cdp_neighbors(f.read()))