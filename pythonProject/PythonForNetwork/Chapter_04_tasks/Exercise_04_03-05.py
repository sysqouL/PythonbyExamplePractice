# ---------------------------------------
"""                                   """
"""

"""
# Задание 4.3 - глава Типы данных в Python. Получить список vlan из строки.
"""

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
tmpl = config.split()               # split - разбивает строку на части, исп-я разделитель (в данном случае пробел) и возвращ-т список строк
print("Строка как список:",tmpl)
vlan = tmpl[-1].split(',')
print("Список vlan'ов:",vlan)
print()

"""
# Задание 4.4 - глава Типы данных в Python. Получить из списка vlan'ов уникальный список, отсортированный по возрастанию номеров.
"""

vlans = [10, 20, 30 , 1, 2, 100, 30, 3, 4, 10]
set1 = set(vlans)                   # из списка делаем множество, для уникальности элементов
print("Список: ",vlans)
print("Множество: ",sorted(set1))   # исп sorted что бы отсортировать множество по возрастанию элементов

"""
# Задание 4.5 - глава Типы данных в Python. Получить из 2 списков vlan'ов пересечение элементов
"""
"""
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
tmpl1 = command1.split()            # разбиваем, возвращаем список строк
tmpl2 = command2.split()            # разбиваем, возвращаем список строк
print("Строка как список:",tmpl1)
print("Строка как список:",tmpl2)
print()

vlan1 = tmpl1[-1].split(',')        # разбиваем, возвращаем список с номерами vlan'ов
vlan2 = tmpl2[-1].split(',')        # разбиваем, возвращаем список с номерами vlan'ов
print("Список vlan'ов 1:",vlan1)
print("Список vlan'ов 2:",vlan2)
print()

set1 = set(vlan1)                   # преобразуем список в множество
set2 = set(vlan2)                   # преобразуем список в множество
print("Множество vlan'ов 1:",set1)
print("Множество vlan'ов 2:",set2)
print()

# Пересечение множеств можно получить с помощью метода intersection() или оператора &
result1 = set1.intersection(set2)
result2 = set1&set2
print("Пересечение vlan'ов c использованием intersection: ",sorted(result1))
print("Пересечение vlan'ов с использование &: ",sorted(result2))

