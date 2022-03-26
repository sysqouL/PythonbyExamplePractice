#-------------------------------------------------
"""
"""

"""
    Задание 6.2, 6.2a, 6.2b
    6.2 - запросить ввод ip адреса в формате - 10.0.1.1. В зависимости от типа адреса, вывести тип введенного адреса
    6.2а - проверки введнного значения: состоит из чисел, каждое число в диапазоне от 0 до 255
    6.2b - используя цикл while сделать возможность повторного ввода ip
"""

while True:
    ip = input("Введите IP адрес: ")
    octets = ip.split('.')
    correct_ip = True
    if len(octets) == 4:
        for i in octets:
            if not (i.isdigit() and 0 <= int(i) <= 255):
                correct_ip = False
                break
    else:
        correct_ip = False
    if correct_ip:
       break
    print("Неверный IP")


if ip == "255.255.255.255":
    print("Это local broadcast адрес")
elif ip == "0.0.0.0":
    print("Это unassigned адрес")
elif int(octets[0]) >= 1 and int(octets[0]) <= 223:
    print("Это unicast адрес")
elif int(octets[0]) >= 224 and int(octets[0]) <= 239:
    print("Это multicast адрес")
else:
    print(f"Это {ip} - unused адрес")

