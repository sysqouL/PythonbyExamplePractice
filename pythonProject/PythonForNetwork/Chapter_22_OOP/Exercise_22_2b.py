#-------------------------------------------------
"""
"""

"""
    Задание 22.2b
    Скопировать класс CiscoTelnet из задания 22.2a и добавить метод send_config_commands.
    Метод send_config_commands должен уметь отправлять одну команду конфигурационного
    режима и список команд.
    Метод должен возвращать вывод аналогичный методу send_config_set у netmiko
    (пример вывода ниже).
    Пример создания экземпляра класса:
    In [1]: from task_22_2b import CiscoTelnet
    In [2]: r1_params = {
       ...:     'ip': '192.168.100.1',
       ...:     'username': 'cisco',
       ...:     'password': 'cisco',
       ...:     'secret': 'cisco'}
    In [3]: r1 = CiscoTelnet(**r1_params)
    Использование метода send_config_commands:
    In [5]: r1.send_config_commands('logging 10.1.1.1')
    Out[5]: 'conf t
    Enter configuration commands, one per line.  End with CNTL/Z.
    R1(config)#logging 10.1.1.1
    R1(config)#end
    R1#'
    In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
    Out[6]: 'conf t
    Enter configuration commands, one per line.  End with CNTL/Z.
    R1(config)#interface loop55
    R1(config-if)#ip address 5.5.5.5 255.255.255.255
    R1(config-if)#end
    R1#'
"""

import time
import telnetlib
from textfsm import clitable
from pprint import pprint


class CiscoTelnet:
    def __init__(self, ip, username, password): #(secret для cisco)
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self._write_line(username)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self._write_line("system-view")
        #self.telnet.read_until(b"Password:") для cisco
        #self._write_line(secret) для cisco
        #self._write_line("terminal length 0")
        time.sleep(1)
        self.telnet.read_very_eager()

    def _write_line(self, line):
        self.telnet.write(line.encode("ascii") + b"\n")

    def send_show_command(self, command, parse=True, templates="templates", index="index"):
        self._write_line(command)
        time.sleep(1)
        command_output = self.telnet.read_very_eager().decode("ascii")
        if not parse:
            return command_output
        attributes = {"Command": command, "Vendor": "huawei_vrp"}
        cli = clitable.CliTable("index", templates)
        cli.ParseCmd(command_output, attributes)
        return [dict(zip(cli.header, row)) for row in cli]

    def send_config_commands(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        commands = ["system-view", *commands, "quit"]
        for command in commands:
            self._write_line(command)
            time.sleep(1)
        return self.telnet.read_very_eager().decode("ascii")

if __name__ == "__main__":
    r1_params = {
        "ip": "192.168.75.133",
        "username": "huawei",
        "password": "huawei",
        # "secret": "cisco",
    }
    r1 = CiscoTelnet(**r1_params)
    with_parse = r1.send_show_command("disp ip int br")
    no_parse = r1.send_show_command("disp ip int br", parse=False)
    list_commands = r1.send_config_commands(
            ["interface Loop1", "ip address 1.1.1.1 255.255.255.254"])
    pprint(with_parse)
    print()
    pprint(no_parse)
    print()
    pprint(list_commands)