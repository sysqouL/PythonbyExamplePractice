#-------------------------------------------------
"""
"""

"""
    Пример класса, который описывает сеть
"""
import ipaddress
class Network:
    all_allocated_ip = []

    def __init__(self, network):
        self.network = network
        self.hosts = tuple(str(ip) for ip in ipaddress.ip_network(network).hosts())
        self.allocated = []

    def allocate(self, ip):
        if ip in self.hosts:
            if ip not in self.allocated:
                self.allocated.append(ip)
                type(self).all_allocated_ip.append(ip)
            else:
                raise ValueError(f"IP-адрес {ip} уже находится в allocated")
        else:
            raise ValueError(f"IP-адрес {ip} не входит в сеть {self.network}")

if __name__ == "__main__":
    net1 = Network(input("Введите сеть 1 в формате ip/маска: "))
    net2 = Network(input("Введите сеть 2 в формате ip/маска: "))
    Again = True
    while Again:
        net1.allocate(str(input("Введите IP для 1 сети: ")))
        net2.allocate(str(input("Введите IP для 2 сети: ")))
        shownet = input("Вывести IP адрса ? Yes/No: ")
        if shownet.lower() == "yes":
            print("Сеть 1:",net1.allocated)
            print("Сеть 2:",net2.allocated)
            print("-----------------------------")
            print("Все добавленные IP:", Network.all_allocated_ip)
        end = input("Еще IP ? Yes/No: ")
        if end.lower() == "no":
            Again = False

