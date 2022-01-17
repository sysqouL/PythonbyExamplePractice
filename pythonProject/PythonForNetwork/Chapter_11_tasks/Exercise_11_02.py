#-------------------------------------------------
"""
"""

"""
    Задание 11.2
    Создать функцию create_network_map, которая обрабатывает вывод команды show cdp neighbors из
    несокльких файлов и объединяет его в одну общую топологию
    У функции должен быть один параметр filenames, который ожидает как аргумент
    список с именами файлов, в которых находится вывод команды sh cdp neighbors
    Функция должна возвращать словарь, который описывает соединения между устройствами.
"""

from Exercise_11_01 import parse_cdp_neighbors
# ppprint - при выводе сохраняет структуру объекта и содержимое
from pprint import pprint


infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    net_map = {}
    for file in filenames:
        with open(file) as sh_cdp:
            pars = parse_cdp_neighbors(sh_cdp.read())
            # добавляем в словарь содержимое другого словаря
            net_map.update(pars)
    return net_map



if __name__ == "__main__":
    topology = create_network_map(infiles)
    pprint(topology)