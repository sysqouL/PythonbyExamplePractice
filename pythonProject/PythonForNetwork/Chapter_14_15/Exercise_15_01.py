#-------------------------------------------------
"""
"""

"""
    Задание 15.1
    Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
    в котором находится конфигурация устройства.
    Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
    которые настроены на интерфейсах, в виде списка кортежей:
    * первый элемент кортежа - IP-адрес
    * второй элемент кортежа - маска
    Для получения такого результата, используйте регулярные выражения.
"""

import re
from pprint import pprint

def get_ip_from_cfg(config):
    """
    - метод groups() возвращает кортеж со строками, в котором эл-ты - те подстроки
      которые попали в соответствующие группы
    - finditer() используется для поиска всех непересекающихся совпадений в шаблоне
    :param config: файл с конфигурацией
    :return: result - кортеж вида IP:Маска
    """
    regex = r"ip address (\S+) (\S+)"
    result = []
    with open(config) as f:
        # аналогичный результата можно получить с помощью генератора списков
        # result = [match.groups() for match in re.finditer(regex, f.read())]
        for match in re.finditer(regex, f.read()):
            result.append(match.groups())
    return result

if __name__ == "__main__":
    pprint(get_ip_from_cfg("config_r1.txt"))