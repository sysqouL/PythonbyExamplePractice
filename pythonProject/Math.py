""" 27 Exercise
num = float(input("Enter number: "))
result = num * 2
print(result)
"""

""" 28 Exercise вывод с округлением
num = float(input("Enter number: "))
result = num * 2
print(round(result, 2))
"""

""" 29 Exercise квадратный корень
import math
num = int(input("Введите целое число больше 500: "))
result = math.sqrt(num)
print(round(result, 2))
"""

""" 30 Exercise число Пи
import math
result = math.pi
print(round(result, 5))
"""

""" 31 Exercise Площадь
import math
radius1 = int(input("Введите радиус круга - "))
area = math.pi * (radius1**2)
print(area)
"""

""" 32 Exercise Объём цилиндра
import math
radius = int(input("Введите радиус - "))
height = int(input("Введите высоту - "))
area = math.pi * (radius**2)
volume = area * height
print(round(volume, 3))
"""

""" 32 Exercise Деление и остаток
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
delenie = num1 // num2
ostatok = num1 % num2
print("Если разделить", num1, "на", num2, "получится", delenie, "с остатком", ostatok)
"""

""" 33 Exercise Площадь квадрата и треугольника
print("1) Square")
print("2) Triangle")
print()
selection = int(input("Введите число: "))
if selection == 1:
    side = int(input("Введите длину стороны квадрата: "))
    area1 = side * side
    print("Площадь квадрата равна -", area1)
elif selection == 2:
    base = int(input("Введите длину стороны треугольника: "))
    height = int(input("Введите высоту треугольника: "))
    area2 = (base * height) / 2
    print("Площадь треугольника равна -", area2)
else:
    print("Некорректный ввод")
"""

