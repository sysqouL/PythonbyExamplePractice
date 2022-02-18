#-------------------------------------------------
"""
"""

"""
    Задание 18.2b
    Скопировать функцию send_config_commands из задания 18.2a и добавить проверку на ошибки.
    При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
     * Invalid input detected, Incomplete command, Ambiguous command
    Если при выполнении какой-то из команд возникла ошибка, функция должна выводить
    сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла,
    при выполнении какой команды и на каком устройстве, например:
    Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
    Ошибки должны выводиться всегда, независимо от значения параметра log.
    При этом, параметр log по-прежнему должен контролировать будет ли выводиться сообщение
"""

from netmiko import ConnectHandler
import yaml
import re
from pprint import pprint

# списки команд:
commands_with_errors = ["disp ip int brf", "sh ver", "i"]
correct_commands = ["disp ssh server status", "disp telnet server status"]
commands = commands_with_errors + correct_commands


def send_config_commands(device, cfg_commands, log=True):
    """

    :param device: список устройств
    :param commands: список команд как корректных так и нет
    :param log: информация о том к какому устройству выполняется подключение
    :return:
    """
    good_commands = {}
    bad_commands = {}
    error_message = 'Команда "{}" выполнилась с ошибкой "{}" на устройстве {}'
    regex = "(?P<errmsg>Error:.+)"
    if log:
        print(f"\nПодключаюсь к {device['host']}...:")
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in cfg_commands:
                result = ssh.send_config_set(command)
                error_in_result = re.search(regex, result)
                if error_in_result:
                    pprint(error_message.format(command, error_in_result.group("errmsg"), ssh.host))
                    bad_commands[command] = result
                else:
                    good_commands[command] = result
        return good_commands, bad_commands

if __name__ == "__main__":
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_config_commands(dev, commands))