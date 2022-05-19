#-------------------------------------------------
"""
"""

"""
    Задание 24.2c
    Скопировать класс MyNetmiko из задания 24.2b.
    Проверить, что метод send_command кроме команду, принимает еще и дополнительные
    аргументы, например, strip_command.
    Если возникает ошибка, переделать метод таким образом, чтобы он принимал
    любые аргументы, которые поддерживает netmiko.
    In [2]: from task_24_2c import MyNetmiko
    In [3]: r1 = MyNetmiko(**device_params)
    In [4]: r1.send_command('sh ip int br', strip_command=False)
    Out[4]: 'sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.1   YES NVRAM  up                    up      
    Ethernet0/1                192.168.200.1   YES NVRAM  up                    up      
    Ethernet0/2                190.16.200.1    YES NVRAM  up                    up      
    Ethernet0/3                192.168.230.1   YES NVRAM  up                    up      
    Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up      
    Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up      
    Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '
    In [5]: r1.send_command('sh ip int br', strip_command=True)
    Out[5]: 'Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.1   YES NVRAM  up                    up      
    Ethernet0/1                192.168.200.1   YES NVRAM  up                    up      
    Ethernet0/2                190.16.200.1    YES NVRAM  up                    up      
    Ethernet0/3                192.168.230.1   YES NVRAM  up                    up      
    Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up      
    Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up      
    Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '
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
        commands_output = commands_output + self.config_mode()
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            commands_output = result + commands_output
            self._check_error_in_command(command, result)
        commands_output = commands_output +self.exit_config_mode()
        return commands_output
