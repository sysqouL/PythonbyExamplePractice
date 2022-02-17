#-------------------------------------------------
"""
"""

"""
    Задание 18.2a
    Скопировать функцию send_config_commands из задания 18.2 и добавить параметр log,
    который контролирует будет ли выводится на стандартный поток вывода информация о том
    к какому устройству выполняется подключение.
    По умолчанию, результат должен выводиться.
"""

from netmiko import ConnectHandler
import yaml

commands = ["disp ssh server status", "disp ip int br", "disp fan"]

def send_config_commands(device, commands, log=True):
    """
    :param device: словарь с параметрами подключения
    :param config_commands: список команд для выполнения
    :return:
    """
    if log:
        print(f"\nПодключаюсь к {device['host']}...:")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)
        return result


if __name__ == "__main__":
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_config_commands(dev, commands))
