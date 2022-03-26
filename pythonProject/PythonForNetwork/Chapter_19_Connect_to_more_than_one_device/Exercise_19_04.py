#-------------------------------------------------
"""
"""

"""
    Задание 19.4
    Создать функцию send_commands_to_devices, которая отправляет команду show или config
    на разные устройства в параллельных потоках, а затем записывает вывод команд в файл.
    Параметры функции:
    * devices - список словарей с параметрами подключения к устройствам
    * filename - имя файла, в который будут записаны выводы всех команд
    * show - команда show, которую нужно отправить (по умолчанию, значение None)
    * config - команды конфигурационного режима, которые нужно отправить (по умолчанию None)
    * limit - максимальное количество параллельных потоков (по умолчанию 3)
    Функция ничего не возвращает.
    Аргументы show, config и limit должны передаваться только как ключевые. При передачи
    этих аргументов как позиционных, должно генерироваться исключение TypeError.
    При вызове функции send_commands_to_devices, всегда должен передаваться
    только один из аргументов show, config. Если передаются оба аргумента, должно
    генерироваться исключение ValueError.
"""

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed

from netmiko import ConnectHandler, NetMikoTimeoutException
import yaml


def send_show_command(device, command_show):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command_show)
        prompt = ssh.find_prompt()
    return f"{prompt}{command_show}\n{result}\n"


def send_cfg_commands(device, command_cfg):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(command_cfg)
    return f"{result}\n"


def send_commands_to_devices(devices, filename, *, show=None, config=None, limit=3):
    if show and config:
        raise ValueError("Можно передавать только один из аргументов show/config")
    command = show if show else config
    function = send_show_command if show else send_cfg_commands

    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(function, device, command) for device in devices]
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())


if __name__ == "__main__":
    command = "disp ver"
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)
    send_commands_to_devices(devices, show=command, filename="result4.txt")
    send_commands_to_devices(devices, config="dhcp enable", filename="result4.txt")