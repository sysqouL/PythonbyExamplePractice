#-------------------------------------------------
"""
"""

""" Тестовые примеры работы с файлами:

result = {}
with open('sh_ip_int_br.txt') as f:
    for line in f:
        line = line.split()
        print(line)
        if line and line[1][0].isdigit():
            interface,address, *other,status = line
            result[interface] = address,status
print(result)

-------------------------------------------------

result = {}
with open('sh_ip_int.txt') as f:
    for line in f:
        if 'line protocol' in line:
            interface = line.split() [0]
        elif "Internet address" in line:
            ip_add = line.split()[3]
            result[interface] = {}
            result[interface]['ip'] = ip_add
        elif 'MTU' in line:
            mtu = line.split() [2]
            result[interface]['mtu'] = mtu
            # print(f'{interface:15}{ip_add:20}{mtu}')
print(result)
"""

"""
    Задание 7.1 - обработать строки из файла ospf.txt и вывести информацию по каждой строке в заданном виде
"""

test = "\n{:20}{}" * 5
with open('ospf.txt', 'r') as f:
    for line in f:
        line = line.replace('['," ").replace(']'," ").replace(","," ").split()
        print(test.format(
        "Prefix", line[0],
        "AD/Metric", line[1],
        "Next-Hop", line[3],
        "Last update", line[4],
        "Outbound Interface", line[5]))

