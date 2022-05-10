#-------------------------------------------------
"""
"""

"""
    Задание 22.1c
    Изменить класс Topology из задания 22.1b.
    Добавить метод delete_node, который удаляет все соединения с указаным устройством.
    Если такого устройства нет, выводится сообщение "Такого устройства нет".
    Создание топологии
    In [1]: t = Topology(topology_example)
    In [2]: t.topology
    Out[2]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    Удаление устройства:
    In [3]: t.delete_node('SW1')
    In [4]: t.topology
    Out[4]:
    {('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    Если такого устройства нет, выводится сообщение:
    In [5]: t.delete_node('SW1')
    Такого устройства нет
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

    def delete_link(self, from_port, to_port):
        if self.topology.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")

    def delete_node(self, node):
        original_size = len(self.topology)
        for src, dest in list(self.topology.items()):
            if node in src or node in dest:
                del self.topology[src]
        if original_size == len(self.topology):
            print("Такого устройства нет")

if __name__ == "__main__":
    topology_example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),}
    top = Topology(topology_example)

    while True:
        print()
        print(" ---------------------------------------------")
        print(" 1 - Вывести топологию сети")
        print(" 2 - Удалить линк в топологии")
        print(" 3 - Удалить узел из топологии")
        print(" 4 - Выход")
        print(" ---------------------------------------------")
        print()
        choice = int(input("Выберете пункт меню: "))
        if choice == 1:
            print()
            print("Топология сети: ")
            pprint(top.topology)
            print()
        elif choice == 2:
            link_from = input("Имя устройства источника: "), input("Порт устройства источника: "),
            link_to = input("Имя устройства назначения: "), input("Порт устройства назначения: "),
            print()
            print("Удалямая запись топологии:", link_from, ',', link_to)
            top.delete_link(link_from, link_to)
            print("Топология сети после удаления: ")
            pprint(top.topology)
        elif choice == 3:
            node = input("Выберите устройство для удаления: ")
            print()
            top.delete_node(node)
            print("Топология сети после удаления устройства: ")
            pprint(top.topology)
        elif choice == 4:
            print()
            print(" -----------BYE----------- ")
            break
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            print("Неправильный пункт меню")

