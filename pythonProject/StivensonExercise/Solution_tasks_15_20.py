#-------------------------------------------------
"""
    Стивенсон Python. Сборник задач.
"""

"""
    Задание №15. Пересчёт расстояния


lenght = int(input("Введите расстояние в футах: "))
inch = lenght * 12
yard = lenght / 3
mile = lenght / 5280

print(f"Введённое расстояние - {lenght} в дюймах - {inch}")
print(f"Введённое расстояние - {lenght} в ярдах - {yard}")
print(f"Введённое расстояние - {lenght} в милях - {mile}")
"""
#-------------------------------------------------


#-------------------------------------------------
"""
    Задание №16. Вычислить площадь круга и объём шара с заданным радиусом


from math import pi

radius = int(input("Введите значение радиуса: "))
area = radius**2*pi
volume = 4/3*pi*radius**3

print(f"Площадь круга = {area}")
print("Площадь шара = {}".format(volume))
"""
#-------------------------------------------------


#-------------------------------------------------
"""
    Задание №17. Теплоемкость. Вычислить количество энергии для нагрева, и стоймость нагрева


volume = float(input("Объём воды в миллилитрах: "))
delta_temp = float(input("Повышение температуры в цельсиях: "))
capacity = 4.186
price = 8.9
j_kwh = 2.777e-7

print()
q = volume * delta_temp * capacity                              # количество энергии в джоулях
print(f"Для нагрева {volume} миллилитров воды, потребуется {q} Дж энергии")

kwh = q * j_kwh
cost = kwh * price                                              # стоимость нагрева
print(f"Стоимость энергии: {round(cost, 4)} центов")
"""
#-------------------------------------------------


#-------------------------------------------------
"""
     Задание №18. Вычислить объём цилиндра


from math import pi

radius = int(input("Введите радиус цилиндра: "))
height = int(input("Введите высоту цилиндра: "))

area = radius*2*pi
volume = area * height

print("Объём цилиндра = {}".format(round(volume,1)))
"""
#-------------------------------------------------


#-------------------------------------------------
"""
    Задание №19. Свободное падение. Вычислить скорость при ударе


from math import sqrt

g = 9.8
height = float(input("Введите высоту с которой бросаем(в метрах): "))
speed = sqrt(2*g*height)

print(f"Скорость объекта при ударе = {round(speed,2)} м/с")
"""
#-------------------------------------------------


#-------------------------------------------------
"""
    Задание №20. Вычисление количества газа в молях при заданных параметрах
    PV = nRT
"""

R = 8.314
P = float(input("Введите значение давления в Па: "))
V = float(input("Введите объём в литрах: "))
Tk = float(input("Введите температуру в кельвинах: "))
Tc = Tk - 273.15

n = (P*V) / (R*Tc)
print (f"Количество вещества - {n} в молях")

