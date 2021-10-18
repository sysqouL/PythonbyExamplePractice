# ---------------------------------------
# Работа с массивами
"""
"""


"""
# from array import *  -  для использования библиотеки массивов
  nums = array ('i', [45,213,414,541,25])  -  создается массив с целочисленным типом данных
  nums.append(значение)  -  добавляет новое число в конец массива
  nums.reverse()  -  переставляет элементы массива в обратном порядке
  nums = sorted(nums)  -  сортирует массив по возрастанию
  nums.pop()  -  удаляет последний элемент массива
  nums.extend(другой массив)  -  объединение массивов
  nums.remove(элемент)  -  удаляет первый элемент массива, совпадающий с введеным в ()
  print(nums.count(30))  -  выводит сколько раз значение 30 встречается в массиве
"""


# ---------------------------------------
"""
# 88 Массив с выводом в обратном порядке

from array import *

newArray = array('i',[])

for i in range(0, 5):
    value = int(input("Введите целое число - "))
    newArray.append(value)

newArray = sorted(newArray)
newArray.reverse()

print(newArray)
"""
# ---------------------------------------


# ---------------------------------------
"""
# 89 Массив случайных чисел

from array import *
import random

newArray = array('i',[])

for i in range(0,5):
    value = random.randint(1, 100)
    newArray.append(value)

for x in newArray:
    print(x)
"""
# ---------------------------------------


# ---------------------------------------
"""
# 90 Массив с условиями ввода

from array import *

newArray = array('i',[])

for i in range(0,5):
    value = int(input("Введите целые числа от 10 до 20: "))
    if value >= 10 and value <= 20:
        newArray.append(value)
    else:
        print("Введенное число выходит за границы")

print("Спасибо !!!")

for x in newArray:
    print(x)
"""
# ---------------------------------------


# ---------------------------------------
"""
# 91 Массив, подсчёт количества вхождений

from array import *

newArray = array('i',[5, 8, 17, 55, 55])
print("Массив - ", newArray)

value = int(input("Введите число - "))
print("Количество вхождений числа",value, "в массив =", newArray.count(value))
"""
# ---------------------------------------


# ---------------------------------------
"""
# 92 Объединение массивов

from array import *
import random

arrayone = array('i',[])
arraytwo = array('i',[])

for i in range(0,3):
    valueone = int(input("Введите числа для первого массива: "))
    arrayone.append(valueone)
print()
print("Первый массив -",arrayone)

for x in range(0,5):
    valuetwo = random.randint(1,555)
    arraytwo.append(valuetwo)
print()
print("Второй массив -",arraytwo)

arrayone.extend(arraytwo)
arraysort = sorted(arrayone)
print()
print("Элементы объеденненого отсортированного массива:")
for y in arraysort:
    print(y)
"""
# ---------------------------------------


# ---------------------------------------
"""
# 93 Удаление элементов массива

from array import *

oldArray = array('i',[])
newArray = array('i',[])

while len(oldArray) < 5:
    value = int(input("Введите целое число: "))
    oldArray.append(value)
    oldArray = sorted(oldArray)

print()
print("Отсортированное содержимое исходного массива:")
for i in oldArray:
    print(i)

choice = int(input("Выберите число из массива: "))
if choice in oldArray:
    oldArray.remove(choice)
    newArray.append(choice)
    print()
    print("Исходный массив:",oldArray)
    print("Новый массив из удаленных элементов:",newArray)
else:
    print("Числа нет в исходном массиве")
"""
# ---------------------------------------


# ---------------------------------------
"""
# 94 Позиция элемента в массиве

from array import *

arrayone = array('i',[54, 78, 124, 8, 19])
print("Исходный массив:",arrayone)
print()
choice = int(input("Введите число из массива: "))
value = False

while value == False:
    if choice in arrayone:
        print("Позиция выбранного числа в массиве -",arrayone.index(choice))
        value = True
    else:
        print("Введенного числа нет в массиве")
        print()
        choice =int(input("Попробуйте ввести число еще раз: "))
"""
# ---------------------------------------


# ---------------------------------------
"""
# 95 Деление элементов массива

from array import *


arrayone = array('f',[48.35, 69.15, 47.32, 29.67, 76.55])
again = True

while again == True:
    choice = int(input("Введите целое число от 2 до 5: "))
    if choice > 5 and choice < 2:
        print("Введенное значение не попадает в диапазон !!!")
    else:
        again = False
print("Исходный массив -",arrayone)
for i in range(0,len(arrayone)):
    res = arrayone[i] / choice
    print("Результата деления элемента",arrayone[i],"на число",choice,"=",round(res, 2))
"""
# ---------------------------------------


