#-------------------------------------------------
"""
"""

"""
    Задание 15.1а
    Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
    чтобы она возвращала словарь:
        * ключ: имя интерфейса
        * значение: кортеж с двумя строками:
            * IP-адрес
            * маска
    В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

"""

import re
from pprint import pprint


def get_ip_from_cfg(config):
    """
    - используются именованные группы, регулярное выражение не обязательно
    компилировать через re.compile
    :param config:
    :return: result - словарь вида {Интерфейс:(Ip, MASK)}
    """
    result = {}
    regex = re.compile(
        r'interface (?P<intf>\S+)\n'
        r'( .*\n)*'
        r' ip address (?P<ip>\S+) (?P<mask>\S+)'
    )
    with open(config) as f:
        # аналогичный результат можно получить через генератор словаря
        # match = re.finditer(regex, f.read())
        # result = {m.group("intf"): m.group("ip", "mask") for m in match}
        for match in re.finditer(regex, f.read()):
            interface = match.group('intf')
            result[interface] = match.group('ip', 'mask')
    return result

if __name__ == "__main__":
    pprint(get_ip_from_cfg("config_r1.txt"))