#-------------------------------------------------
"""
"""

"""
    Задание 24.2b
    Скопировать класс MyNetmiko из задания 24.2a.
    Дополнить функционал метода send_config_set netmiko и добавить в него проверку
    на ошибки с помощью метода _check_error_in_command.
    Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
    Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает
    вывод команд.
    In [2]: from task_24_2b import MyNetmiko
    In [3]: r1 = MyNetmiko(**device_params)
    In [4]: r1.send_config_set('lo')
    ---------------------------------------------------------------------------
    ErrorInCommand                            Traceback (most recent call last)
    <ipython-input-2-8e491f78b235> in <module>()
    ----> 1 r1.send_config_set('lo')
    ...
    ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."
"""

import re
from netmiko.cisco.cisco_ios import CiscoIosSSH
from Exercise_24_2a import ErrorInCommand


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, result):
        regex = "(?P<errmsg>Error:.+)"
        error_message = (
            'При выполнении команды "{cmd}" на устройстве {device} возникла ошибка -> {error}"'
        )
        error_in_result = re.search(regex, result)
        if error_in_result:
            raise ErrorInCommand(
                error_message.format(cmd=command, device=self.host, error=error_in_result.group("errmsg"))
            )

    def send_command(self, command, *args, **kwargs):
        command_output = super().send_command(command, *args, **kwargs)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self, commands):
        # если commands строкой(экземпляром класа str)
        if isinstance(commands, str):
            commands = [commands]
        commands_output = ""
        self.config_mode()
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            commands_output = result + commands_output
            self._check_error_in_command(command, result)
        self.exit_config_mode()
        return commands_output
