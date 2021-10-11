""" №3 Площадь комнаты
lenght = float(input("Введите длинну комнаты - "))
width = float(input("Введите ширину комнаты - "))
area = lenght * width
print("Площадь комнаты =", area,"м.кв")
"""

""" №4 Площадь садового участка
lenght = float(input("Введите длинну садового участка в футах - "))
width = float(input("Введите ширину садового участка в футах - "))
area = lenght * width
print("Площадь участка - ", area // 43560, " акров")
"""

""" №5 Бутылки
litryxa = int(input("Количество бутылок обьёмом 1 литр и меньше - "))
bolshelitra = int(input("Количество бутылок больше литра - "))
result = (litryxa * 0.10) + (bolshelitra * 0.25)
print("Сдав бутылки можно получить $%.2f" % result)
"""

""" №6 Налоги и чаевые
sumzakaza = int(input("Сумма заказа в ресторане: "))
nalog = sumzakaza * 0.07
chaevie = sumzakaza * 0.18
result = sumzakaza + nalog + chaevie
print("Итоговая сумма вашего заказа - $%.2f" % result, "включая налог - $%.2f" % nalog, "и чаевые - $%.2f" % chaevie)
"""

""" №7 Сумма первых n положительных чисел
num1 = int(input("Введите положительное число - "))
sum = ((num1)*(num1+1)) / 2
print("Сумма первых", num1, "положительных чисел равна", sum)
"""

""" №8 Сувениры и безделушки
suvenir = int(input("Количество купленных сувениров: "))
bezdel = int(input("Количество купленных безделушек: "))
ves = (suvenir * 75) + (bezdel * 112)
print("Общий вес посылки -", ves, "в граммах")
"""

""" №9 Депозит счёт
perv_vznos = float(input("Введите сумму первоночального депозита - "))
cherez_god = round((perv_vznos * 1.04),2)
cherez_dva = round((cherez_god * 1.04),2)
cherez_tri = round((cherez_dva * 1.04),2)
print("Сумма на счету через год - руб", cherez_god,"\nЧерез два года - руб", cherez_dva,"\nЧерез три года - руб", cherez_tri)
"""

""" №10 Арифметика
from math import log10
a = int(input("Введите целое число а - "))
b = int(input("Введите целое число b - "))
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
print(a, "/", b, "=", a / b)
print(a, "%", b, "=", a % b)
print(a, "в степени", b, "=", a ** b)
print("Десятичный логарифм числа", a, "=", log10(a))
"""


""" №11 Потребление топлива 
мили на галон перевести в литры на 100 км
Литры на 100км = 100 * литров в галлоне(3.785) / мили на галлон * км в миле(1.609)

import math
MPG = float(input("Введите показатель потребления топлива в милях на галлон - "))
LPK = (100 * 3.785) / (MPG * 1.609)
print("Потребление топлива - л/100км - ", round(LPK, 4))
"""

import math
st1 = float(input("Введите широту первой точки в градусах - "))
dt1 = float(input("Введите долготу первой точки в градусах - "))
st2 = float(input("Введите широту второй точки в градусах - "))
dt2 = float(input("Введите долготу второй точки в градусах - "))

distance = 6371.01 * math.radians(math.acos((math.sin(st1) * math.sin(st2) + math.cos(st1) * math.cos(st2) * math.cos(dt1 - dt2))))
print("Расстояние между точками при следовании по кратчайшему пути по поверхности планеты ", round(distance,4), " км")