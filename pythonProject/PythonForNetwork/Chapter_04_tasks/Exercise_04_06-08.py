"""
# Задание 4.6 - глава Типы данных в Python. Обработать строку ospf_route и вывести информацию в заданном виде
"""
"""
ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

tmpl = ospf_route.replace('[','').replace(']','').replace(',','')
tmpl = tmpl.split()
result = "\n{:20} {}" * 5
print(result.format(
        "Prefix", tmpl[0],
        "AD/Metric", tmpl[1],
        "Next-Hop", tmpl[3],
        "Last update", tmpl[4],
        "Outbound Interface", tmpl[5],
))
"""
"""
"""
# Задание 4.7 - глава Типы данных в Python. Преобразовать MAC адрес в двоичную строку
"""

mac = "AAAA:BBBB:CCCC"
mac_new = mac.replace(':','')
mac_final = "{:b}".format(int(mac_new, 16))
print("Исходный MAC: ",mac)
print("Преобразованный в 2: ",mac_final)
"""
"""
# Задание 4.8 - глава Типы данных в Python. Преобразовать IP адрес в двоичный формат 
"""

ip = "192.168.3.1"
test = ip.split(".")
ip_template = '''
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(ip_template.format(int(test[0]),int(test[1]),int(test[2]),int(test[3])))

