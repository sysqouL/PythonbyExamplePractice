#-------------------------------------------------
"""
"""

"""
    Задание 15.1b
    Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
    образом, чтобы в значении словаря она возвращала список кортежей
    для каждого интерфейса.
    Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
    Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
    несколько кортежей. Ключом остается имя интерфейса.
    Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
    Ethernet0/1 соответствует список из двух кортежей.

"""

import re
from pprint import pprint


def get_ip_from_cfg(config):
    """
    lastgroup() - возвращает имя последней именованной группы в регулярном
    выражении, для которой было найдено совпадение
    setdefault() - метод ищет ключ, и если его нет, создает ключ со значением None

    :param config:
    :return:
    """
    result = {}
    regex = (r"^interface (?P<intf>\S+)"
             r"|address (?P<ip>\S+) (?P<mask>\S+)")
    with open(config) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == "intf":
                    intf = match.group(match.lastgroup)
                elif match.lastgroup == "mask":
                    result.setdefault(intf, [])
                    result[intf].append(match.group("ip", "mask"))
    return result

if __name__ == "__main__":
    pprint(get_ip_from_cfg("config_r2.txt"))