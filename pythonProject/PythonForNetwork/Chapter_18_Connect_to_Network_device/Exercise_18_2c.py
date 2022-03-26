#-------------------------------------------------
"""
"""

"""
    Задание 18.2c
    Скопировать функцию send_config_commands из задания 18.2b и переделать ее таким образом:
    Если при выполнении команды возникла ошибка, спросить пользователя надо ли выполнять
    остальные команды.
    Варианты ответа [y]/n:
    * y - выполнять остальные команды. Это значение по умолчанию,
      поэтому нажатие любой комбинации воспринимается как y
    * n или no - не выполнять остальные команды
    Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
    * первый словарь с выводом команд, которые выполнились без ошибки
    * второй словарь с выводом команд, которые выполнились с ошибками
    Оба словаря в формате
    * ключ - команда
    * значение - вывод с выполнением команд
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
                    continue_command = input("Продолжать выполнять команды? [Yes]/[No]: ")
                    if continue_command.lower() in ( "no", "n"):
                        break
                else:
                    good_commands[command] = result
        return good_commands, bad_commands

if __name__ == "__main__":
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_config_commands(dev, commands))

