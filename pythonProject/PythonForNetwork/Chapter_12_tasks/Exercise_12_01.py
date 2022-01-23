#-------------------------------------------------
"""
"""

"""
    Задание 12.1
    Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
    Функция ожидает как аргумент список IP-адресов.
    Функция должна возвращать кортеж с двумя списками:
    * список доступных IP-адресов
    * список недоступных IP-адресов
"""

import subprocess, ipaddress

ip_list = ["10.1.1.1", "8.8.8.8"]

def ping_ip_address(ip_addresses):
    reachable = []
    unreachable = []
    for ip in ip_addresses:
        result = subprocess.run(['ping', ip],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                # stdout - получить результат выполнения команды
                                # stderr - получить резултат если ошибка выполнения
                                # можно так ['ping', '-c', '4', ip]
        # спец объект CompletedProcess - из него можно получить код возврата
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    print(f"Доступны - {reachable}")
    print(f"Недоступны - {unreachable}")
    return reachable, unreachable

if __name__ == "__main__":
    print(ping_ip_address(ip_list))

