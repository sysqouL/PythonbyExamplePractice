#-------------------------------------------------
"""
"""

"""
    Задание 19.3a
    Создать функцию send_command_to_devices, которая отправляет список указанных
    команд show на разные устройства в параллельных потоках, а затем записывает
    вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.
    Параметры функции:
    * devices - список словарей с параметрами подключения к устройствам
    * commands_dict - словарь в котором указано на какое устройство отправлять
      какие команды. Пример словаря - commands
    * filename - имя файла, в который будут записаны выводы всех команд
    * limit - максимальное количество параллельных потоков (по умолчанию 3)
    Функция ничего не возвращает.
    Вывод команд должен быть записан в файл.
    Порядок команд в файле может быть любым.
"""

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed

from netmiko import ConnectHandler, NetMikoTimeoutException
import yaml

commands = {
    "192.168.75.133": ["disp ip int br", "disp ip int desc"],
    "192.168.75.134": ["disp int desc", "disp int count inb"],
    "192.168.75.135": ["disp ver"],
}

def send_show_command(device, commands):
    output = ""
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        for command in commands:
            result = ssh.send_command(command)
            prompt = ssh.find_prompt()
            output += f"{prompt}{command}\n{result}\n"
    return output


def send_command_to_devices(devices, commands_dict, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = []
        for device in devices:
            ip = device["host"]
            command = commands_dict[ip]
            futures.append(executor.submit(send_show_command, device, command))
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())


if __name__ == "__main__":
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)
    send_command_to_devices(devices, commands, "result3.txt")