#-------------------------------------------------
"""
"""

"""
    Задание 22.1d
    Изменить класс Topology из задания 22.1c
    Добавить метод add_link, который добавляет указанное соединение, если его еще
     нет в топологии.
    Если соединение существует, вывести сообщение "Такое соединение существует",
    Если одна из сторон есть в топологии, вывести сообщение
    "Cоединение с одним из портов существует"
    Создание топологии
    In [7]: t = Topology(topology_example)
    In [8]: t.topology
    Out[8]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    In [10]: t.topology
    Out[10]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    Такое соединение существует
    In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    Соединение с одним из портов существует
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

    def add_link(self, src_port, dst_port):
        topology_area = self.topology.keys() or self.topology.values()
        if self.topology.get(src_port) == dst_port:
            print("Такое соединение существует")
        elif src_port in topology_area or dst_port in topology_area:
            print("Соединение с одним из портов существует")
        else:
            self.topology[src_port] = dst_port


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
        print(" 4 - Добавить линк в топологию")
        print(" 5 - Выход")
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
            source_port = input("Имя устройства источника: "), input("Порт устройства источника: "),
            destination_port = input("Имя устройства назначения: "), input("Порт устройства назначения: "),
            print()
            print("Добавляемая запись в топологии:", source_port,',', destination_port)
            top.add_link(source_port, destination_port)
            print("Топология сети после добавления")
            pprint(top.topology)
        elif choice == 5:
            print()
            print(" -----------BYE----------- ")
            break
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            print("Неправильный пункт меню")