#-------------------------------------------------
"""
"""

"""
Задание 21.2
    Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding
    и записать его в файл templates/sh_ip_dhcp_snooping.template
    Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.
    Шаблон должен обрабатывать и возвращать значения таких столбцов:
    * mac - такого вида 00:04:A3:3E:5B:69
    * ip - такого вида 10.1.10.6
    * vlan - 10
    * intf - FastEthernet0/10
    Проверить работу шаблона с помощью функции parse_command_output из задания 21.1.
"""


import textfsm
from Exercise_21_01 import parse_command_output
from pprint import pprint

if __name__ == "__main__":
    temp = "templates/sh_ip_dhcp_snooping.template"             # "templates/sh_ip_dhcp_snooping_hua.template"
    with open("output/sh_ip_dhcp_snooping.txt") as show:           # "output/sh_ip_dhcp_snooping_hua.txt"
        output = show.read()
    result = parse_command_output(temp, output)
    print()
    pprint(result)