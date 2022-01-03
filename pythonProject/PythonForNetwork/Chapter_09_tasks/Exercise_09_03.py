#-------------------------------------------------
"""
"""

"""
    Задание 9.3 - создать функцию get_int_vlan_map, которая обрабатывает конф файл и 
    возвращает кортеж из 2 словарей: access порты и vlan, trunk порты и vlan
    Задание 9.3а - добавить поддержку конф, когда порт в vlan 1
"""

def get_int_vlan_map(config_filename):
 access_dict = {}
 trunk_dict = {}
 with open(config_filename) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("interface "):
            # название интерфейсов
            intf = line.split()[1]
            # всем интерефейсам ставим vlan 1 как default
            access_dict[intf] = 1
        elif "access vlan" in line:
            # в словарь заносим интерфейс: vlan
            access_dict[intf] = line.split()[-1]
        elif "trunk allowed" in line:
            # в словарь заносим интерфейс: список vlan
            trunk_dict[intf] = [vlan for vlan in line.split()[-1].split(",")]
    return access_dict, trunk_dict