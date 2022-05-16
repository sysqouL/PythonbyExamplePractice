#-------------------------------------------------
"""
"""

"""
    Задание 23.3a
    В этом задании надо сделать так, чтобы экземпляры класса Topology
    были итерируемыми объектами.
    Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.
    После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
    На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
    Порядок вывода соединений может быть любым.
    Пример работы класса:
    In [1]: top = Topology(topology_example)
    In [2]: for link in top:
       ...:     print(link)
       ...:
    (('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
    (('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
    (('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
    (('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
    (('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
    (('R3', 'Eth0/2'), ('R5', 'Eth0/0'))
"""

from pprint import pprint

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        normalized_topology = {}
        for box, neighbor in topology_dict.items():
            if not neighbor in normalized_topology:
                normalized_topology[box] = neighbor
        return normalized_topology

    def __add__(self, other):
        copy_topology = self.topology.copy()
        copy_topology.update(other.topology)
        return Topology(copy_topology)

    def __iter__(self):
        return iter(self.topology.items())

if __name__ == "__main__":
    topology_example_1 = {
         ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
         ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
         ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
         ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
         ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
         ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    topology_example_2 = {
         ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
         ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    top_1 = Topology(topology_example_1)
    top_2 = Topology(topology_example_2)
    while True:
        print()
        print(" ---------------------------------------------")
        print(" 1 - Вывести топологии сетей")
        print(" 2 - Сложить топологии")
        print(" 3 - Проверка итерации")
        print(" 4 - Выход")
        print(" ---------------------------------------------")
        print()
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            print("Топология сети 1: ")
            pprint(top_1.topology)
            print()
            print("Топология сети 2: ")
            pprint(top_2.topology)
            print()
        elif choice == 2:
            finally_top = top_1 + top_2
            print()
            print("Результат сложения топологий:")
            pprint(finally_top.topology)
        elif choice == 3:
            print()
            print("Проверка итерируемых объектов:")
            for link_top_1 in top_1:
                print(f"Соединения первой топологии - {link_top_1}")
            print()
            for link_top_2 in top_2:
                print(f"Соединения второй топологии - {link_top_2}")
        elif choice == 4:
            print("Bye")
            break
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            print("Неправильный пункт меню")

