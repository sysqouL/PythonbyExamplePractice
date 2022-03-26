#-------------------------------------------------
"""
"""

"""
    Задание 15.5
    Создать функцию generate_description_from_cdp, которая ожидает как аргумент
    имя файла, в котором находится вывод команды show cdp neighbors.
    Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
    на основании вывода команды описание для интерфейсов.
    Например, если у R1 такой вывод команды:
        R1>show cdp neighbors
        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                          S - Switch, H - Host, I - IGMP, r - Repeater
        Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
        SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1
    Для интерфейса Eth 0/0 надо сгенерировать такое описание
    description Connected to SW1 port Eth 0/1
    Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
    а значения - команда задающая описание интерфейса:
        'Eth 0/0': 'description Connected to SW1 port Eth 0/1'
"""

import re
from pprint import pprint


def generate_description_cdp(sh_cdp_file):
    """
    [R S I] можно заменить на [\w ]
    :param sh_cdp_file: файл с выводом команды sh cdp neighbors
    :return: result - словарь вида {local_int:'description Connected to {device} port {dest_int}}
    """
    regex = (r"(?P<device>\S+)  +(?P<loc_int>\S+ \S+)"
        r" +\d+  +[R S I]+  +\S+ +(?P<dest_int>\S+ \S+)"
        )
    description = "description Connected to {} port {}"
    result = {}
    with open(sh_cdp_file) as f:
        for match in re.finditer(regex, f.read()):
            device, loc_int, dest_int = match.group("device", "loc_int", "dest_int")
            result[loc_int] = description.format(device, dest_int)
    return result

if __name__ == "__main__":
    pprint(generate_description_cdp("sh_cdp_n_sw1.txt"))
