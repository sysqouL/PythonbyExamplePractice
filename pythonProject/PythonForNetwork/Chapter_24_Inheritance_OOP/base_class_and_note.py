#-------------------------------------------------
"""
"""

"""
    -------------------------------------------------------------------------------------------------------------------------
    Наследование позволяет создавать классы на основе существующих. Различают родительский класс и дочерний - дочерний
    наследует родительский. При наследовании дочерний класс наследует все методы и атрибуты родительского класса.
    Синтаксис:
    
        class <дочерний> (<родительский>)
        вызов метода:
        command = super().<имя метода>(параметры)
"""


"""
    Основной класс для наследования для заданий 24.1x
"""

import netmiko


class BaseSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    def send_cfg_commands(self, commands):
        return self.ssh.send_config_set(commands)