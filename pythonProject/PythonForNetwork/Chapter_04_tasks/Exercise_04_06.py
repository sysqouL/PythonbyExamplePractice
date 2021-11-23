"""
# Задание 4.6 - глава Типы данных в Python. Обработать строку ospf_route и вывести информацию в заданном виде
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

tmpl = ospf_route.replace('[','').replace(']','').replace(',','')
print(ospf_route)
tmpl = tmpl.split()
result = "\n{:20} {}" * 5
print(result.format(
        "Prefix", tmpl[0],
        "AD/Metric", tmpl[1],
        "Next-Hop", tmpl[3],
        "Last update", tmpl[4],
        "Outbound Interface", tmpl[5],
))
