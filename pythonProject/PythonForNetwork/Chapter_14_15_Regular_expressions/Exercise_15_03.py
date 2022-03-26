#-------------------------------------------------
"""
"""

"""
    Задание 15.3
    Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
    из синтаксиса cisco IOS в cisco ASA.
    Функция ожидает такие аргументы:
        - имя файла, в котором находится правила NAT Cisco IOS
        - имя файла, в который надо записать полученные правила NAT для ASA
    Функция ничего не возвращает.
    
    Пример правил NAT cisco IOS
    ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
    ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023
    И соответствующие правила NAT для ASA:
    object network LOCAL_10.1.2.84
     host 10.1.2.84
     nat (inside,outside) static interface service tcp 22 20022
    object network LOCAL_10.1.9.5
     host 10.1.9.5
     nat (inside,outside) static interface service tcp 22 20023
    В файле с правилами для ASA:
        - не должно быть пустых строк между правилами
        - перед строками "object network" не должны быть пробелы
        - перед остальными строками должен быть один пробел
"""

import re
from pprint import pprint

def convert_ios_nat_to_asa(cisco_ios, cisco_asa):
    """
    ** ключевые аргументы переменной длинны в виде словаря из match.groupdict()
    :param cisco_ios: файл конфига IOS
    :param cisco_asa: файл конфига ASA
    :return: нет
    """
    regex = (
        "tcp (?P<local_ip>\S+) +(?P<local_port>\d+) +interface +\S+ (?P<outside_port>\d+)"
    )
    asa_template = (
        "object network LOCAL_{local_ip}\n"
        " host {local_ip}\n"
        " nat (inside,outside) static interface service tcp {local_port} {outside_port}\n"
    )
    with open(cisco_ios) as f, open(cisco_asa, "w") as asa_nat_cfg:
        data = re.finditer(regex, f.read())
        for match in data:
            asa_nat_cfg.write(asa_template.format(**match.groupdict()))
            pprint(match.groupdict())

if __name__ == "__main__":
    convert_ios_nat_to_asa("cisco_nat_config.txt", "cisco_asa_config.txt")
