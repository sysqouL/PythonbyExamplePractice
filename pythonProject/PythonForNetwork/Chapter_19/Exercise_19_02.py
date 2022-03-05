#-------------------------------------------------
"""
"""

"""
    Задание 19.2
    Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
    команду show на разные устройства в параллельных потоках, а затем записывает
    вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.
    Параметры функции:
    * devices - список словарей с параметрами подключения к устройствам
    * command - команда
    * filename - имя текстового файла, в который будут записаны выводы всех команд
    * limit - максимальное количество параллельных потоков (по умолчанию 3)
    Функция ничего не возвращает.
    Вывод команд должен быть записан в обычный текстовый файл
"""

import yaml
from itertools import repeat
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor

def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(send_show_command, devices, repeat(command))
        with open(filename, "w") as f:
            for output in results:
                f.write(output)


if __name__ == "__main__":
    command = "disp curr"
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)
    send_show_command_to_devices(devices, command, "result.txt")