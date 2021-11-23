# ---------------------------------------
"""                                   """


"""
# Задание 4.2 - глава Типы данных в Python. Преобразовать строку mac из XXXX:XXXX:XXXX в XXXX.XXXX.XXXX.
"""

# Замена с помощью replace
mac = "001d:b4fc:47en"
new_mac = mac.replace(":",".")
print("Исходный MAC -",mac)
print("Преобразованный MAC -",new_mac)
print()

# Замена с помощью format
new_mac_format = "001d{zam}b4fc{zam}47en".format(zam='.') # "001d{}b4fc{}47en".format('.','.')
print("Исходный MAC -",mac)
print("Преобразованный MAC, с использованием format: ",new_mac_format)
print()

# Замена с помощью f строк
change ='.'
new_mac_f = f"001d{change}b4fc{change}47en"
print("Исходный MAC -",mac)
print("Преобразованный MAC, с использованием f строки: ",new_mac_f)