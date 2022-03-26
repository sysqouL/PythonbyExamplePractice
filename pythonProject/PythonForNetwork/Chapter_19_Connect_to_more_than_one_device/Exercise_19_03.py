#-------------------------------------------------
"""
"""

"""
    Задание 19.3
    Создать функцию send_command_to_devices, которая отправляет разные
    команды show на разные устройства в параллельных потоках, а затем записывает
    вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.
    Параметры функции:
    * devices - список словарей с параметрами подключения к устройствам
    * commands_dict - словарь в котором указано на какое устройство отправлять
      какую команду. Пример словаря - commands
    * filename - имя файла, в который будут записаны выводы всех команд
    * limit - максимальное количество параллельных потоков (по умолчанию 3)
    Функция ничего не возвращает.
    Вывод команд должен быть записан в файл
"""

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed

from netmiko import ConnectHandler, NetMikoTimeoutException
import yaml


commands = {
    "192.168.75.133": "disp ip int br",
    "192.168.75.134": "disp int desc",
    "192.168.75.135": "disp ver",
}


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_command_to_devices(devices, commands_dict, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        # submit - запускает в потоке только 1 функцию
        # можно запускать разные функции с разными несвязными аргументами
        # возвращается спец объект Future, который представляет выполнение функции
        # можно передавать ключевые аргументы, map - только позиционные
        futures = [
            executor.submit(send_show_command, device, commands_dict[device["host"]])
            for device in devices
        ]
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())


if __name__ == "__main__":
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)
    send_command_to_devices(devices, commands, "result2.txt")