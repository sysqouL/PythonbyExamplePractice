#-------------------------------------------------
"""
"""

"""
    Задание 22.2c
    Скопировать класс CiscoTelnet из задания 22.2b и изменить метод send_config_commands
    добавив проверку команд на ошибки.
    У метода send_config_commands должен быть дополнительный параметр strict:
    * strict=True значит, что при обнаружении ошибки, необходимо сгенерировать
      исключение ValueError (значение по умолчанию)
    * strict=False значит, что при обнаружении ошибки, надо только вывести
      на стандартный поток вывода сообщение об ошибке
    Метод дожен возвращать вывод аналогичный методу send_config_set
    у netmiko (пример вывода ниже). Текст исключения и ошибки в примере ниже.
    Пример создания экземпляра класса:
    In [1]: from task_22_2c import CiscoTelnet
    In [2]: r1_params = {
       ...:     'ip': '192.168.100.1',
       ...:     'username': 'cisco',
       ...:     'password': 'cisco',
       ...:     'secret': 'cisco'}
    In [3]: r1 = CiscoTelnet(**r1_params)
    In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
    In [6]: commands = commands_with_errors+correct_commands
    Использование метода send_config_commands:
    In [7]: print(r1.send_config_commands(commands, strict=False))
    При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
    При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка -> Incomplete command.
    При выполнении команды "a" на устройстве 192.168.100.1 возникла ошибка -> Ambiguous command:  "a"
    conf t
    Enter configuration commands, one per line.  End with CNTL/Z.
    R1(config)#logging 0255.255.1
                       ^
    % Invalid input detected at '^' marker.
    R1(config)#logging
    % Incomplete command.
    R1(config)#a
    % Ambiguous command:  "a"
    R1(config)#logging buffered 20010
    R1(config)#ip http server
    R1(config)#end
    R1#
    In [8]: print(r1.send_config_commands(commands, strict=True))
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-8-0abc1ed8602e> in <module>
    ----> 1 print(r1.send_config_commands(commands, strict=True))
    ...
    ValueError: При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
"""

import time
import telnetlib
import re
from textfsm import clitable
from pprint import pprint


class CiscoTelnet:
    def __init__(self, ip, username, password): #(secret для cisco)
        self.ip = ip
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

    def error_in_command(self, command, result, strict):
        regex = "(?P<errmsg>Error:.+)"
        error_message = ('При выполнении команды "{cmd}" на устройстве {device} возникла ошибка -> {error}"')
        error_in_result = re.search(regex, result)
        if error_in_result:
            message = error_message.format(cmd=command, device=self.ip, error=error_in_result.group("errmsg"))
            if strict:
                raise ValueError(message)
            else:
                print(message)

    def send_config_commands(self, commands, strict=True):
        output = ""
        if isinstance(commands, str):
            commands = [commands]
        commands = ["system-view ", *commands, "return"]
        for command in commands:
            self._write_line(command)
            time.sleep(1)
            result = self.telnet.read_very_eager().decode("ascii")
            output = output + result
            self.error_in_command(command, result, strict=strict)
            output = output + self.telnet.read_very_eager().decode("ascii")
        return output


if __name__ == "__main__":
    r1_params = {
        "ip": "192.168.75.133",
        "username": "huawei",
        "password": "huawei",
        # "secret": "cisco",
    }
    r1 = CiscoTelnet(**r1_params)
    commands_with_errors = ['logging 255.255.255.255', 'b', 'a']
    correct_commands = ["interface Loop1", "ip address 1.1.1.1 255.255.255.255", "disp ip int br"]
    commands = commands_with_errors+correct_commands
    #with_parse = r1.send_show_command("disp ip int br")
    #no_parse = r1.send_show_command("disp ip int br", parse=False)
    list_commands = r1.send_config_commands(commands,strict=False)
    #pprint(with_parse)
    #print()
    #pprint(no_parse)
    print()
    pprint(list_commands)