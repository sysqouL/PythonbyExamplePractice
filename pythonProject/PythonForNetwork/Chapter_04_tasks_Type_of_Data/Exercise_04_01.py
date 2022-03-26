# ---------------------------------------
"""                                   """


"""
# Задание 4.1 - глава Типы данных в Python. Получение новой строки из подготовленной, с заменой имени интерфейса.
"""

# Замена с помощью replace
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print("Исходная строка: ",nat)
nat_new = nat.replace("Fast","Gigagibit")
print("Полученная строка: ",nat_new)
print()

# Замена с помощью format
print("Исходная строка: ",nat)
type_int2 = input("Введите интерфейс (GigabitEthernet/FastEthernet): ")
nat2 = "ip nat inside source list ACL interface {}0/1 overload".format(type_int2)
print("Полученная строка, с использованием format: ",nat2)
print()

# Замена с помощью f строк
print("Исходная строка: ",nat)
type_int3 = input("Выберите тип интерфейса (GigabitEthernet/FastEthernet): ")
nat3 = f"ip nat inside source list ACL interface {type_int3}0/1 overload"
print("Полученная строка, с использованием f строки: ",nat3)
