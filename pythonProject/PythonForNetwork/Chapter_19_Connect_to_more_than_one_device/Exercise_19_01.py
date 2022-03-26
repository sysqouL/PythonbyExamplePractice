#-------------------------------------------------
"""
"""

"""
    Задание 19.1
    Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
    Проверка IP-адресов должна выполняться параллельно в разных потоках.
    Параметры функции ping_ip_addresses:
    * ip_list - список IP-адресов
    * limit - максимальное количество параллельных потоков (по умолчанию 3)
    Функция должна возвращать кортеж с двумя списками:
    * список доступных IP-адресов
    * список недоступных IP-адресов
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor


def ping_ip(ip):
    """
    :param ip: ip адрес
    :return: возвращает доступные
    """
    result = subprocess.run(["ping", "-c", "4", ip], stdout=subprocess.DEVNULL)
    ip_is_reachable = result.returncode == 0
    return ip_is_reachable


def ping_ip_addresses(ip_list, limit=3):
    """

    :param ip_list: список ip
    :param limit: количество параллельных потоков
    :return: доступные и недоступные
    """
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        # map применяет функцию ping_ip к списку ip_list, каждый вызов в отдельном потоке
        results = executor.map(ping_ip, ip_list)
        # для совмещения ip устройств и вывода команд используется zip
    for ip, status in zip(ip_list, results):
        if status:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(["8.8.8.8", "192.168.100.22", "192.168.75.133"]))