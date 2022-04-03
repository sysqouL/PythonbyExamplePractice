#-------------------------------------------------
"""
"""

"""
    Задание 18.1
    Создать функцию send_show_command.
    Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
    и выполняет указанную команду.
    Параметры функции:
    * device - словарь с параметрами подключения к устройству
    * command - команда, которую надо выполнить
    Функция возвращает строку с выводом команды.
    Скрипт должен отправлять команду command на все устройства из файла devices.yaml
    с помощью функции send_show_command (эта часть кода написана).
"""

from netmiko import ConnectHandler
import yaml

def send_show_command(device, command):
    """
    :param device: словарь с параметрами подключения к устройству
    :param command: команда, которую надо выполнить
    :return:
    """
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        return output


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))
