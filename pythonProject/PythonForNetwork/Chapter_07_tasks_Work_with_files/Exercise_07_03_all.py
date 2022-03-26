#-------------------------------------------------
"""
"""

"""
    Задание 7.3 - вывести таблицу MAC из файла MAC_table.txt
    Задание 7.3a - вывод отсортирован по убыванию vlan
    Задание 7.3b - вывод только выбранных vlan
    
"""

mac_table = []
choice_vlan = int(input("Введите номер vlan: "))
with open("MAC_table.txt","r") as f:
    for line in f:
        line = line.split()
        if line and line[0].isdigit():
            vlan,mac,type,ports = line
            mac_table.append([int(vlan),mac,ports])
for vlan,mac,ports in sorted(mac_table):
    if choice_vlan == vlan:
        print("{:<7} {:17} {}".format(choice_vlan,mac,ports))                              # print(f"{vlan:<7} {mac:17} {ports}")
