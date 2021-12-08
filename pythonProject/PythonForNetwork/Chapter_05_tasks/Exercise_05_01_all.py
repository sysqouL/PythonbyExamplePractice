#-------------------------------------------------
"""
# Задание 5.1-a,b,c,d  - глава Создание базовых Скриптов. Работа со словарем устройств
"""

"""
    "разделитель".join(список) - собирает список строк в одну строку с разделителем
"""

""" Пример
interface = input("Введите название интерфейса: ")
vlan = input("Введите номер vlan'a: ")

test_template = ['switchport mode access',
                 'switchport access vlan {}',
                 'switchport nonegotiate',
                 'spanning-tree portfast',
                 'spanning-tree bpduguard enable']
print("\n"+'-'*30)
print('interface {}'.format(interface))
print('\n'.join(test_template).format(vlan))
print("\n"+'-'*30)
"""


london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "7206",
        "ios": "15.04",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "7205",
        "ios": "15.04",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3550",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
print()
devlist = ",".join(london_co.keys())                                        # строка с устройствами
devices = input("Выберете устройство ({}): ".format(devlist))               # отображение списка возможных устройств с помощью format

optionslist = ",".join((london_co[devices]).keys())                         # строка с параметрами
options = str.lower(input(f"Выберете параметр ({optionslist}): "))          # отображение списка параметров с помощью f строк
# print(london_co[devices].get(options, "Такаого параметра нет"))           # проверка правельности ввода параметра


print("Устройство -",devices,"; параметр -",options,"=",london_co[devices][options])
