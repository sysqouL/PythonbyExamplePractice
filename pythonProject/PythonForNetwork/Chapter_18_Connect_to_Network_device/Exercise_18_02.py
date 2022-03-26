#-------------------------------------------------
"""
"""

"""
    Задание 18.2
    Создать функцию send_config_commands
    Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству и выполняет
    перечень команд в конфигурационном режиме на основании переданных аргументов.
    Параметры функции:
    * device - словарь с параметрами подключения к устройству
    * config_commands - список команд, которые надо выполнить
    Функция возвращает строку с результатами выполнения команды
"""



from netmiko import ConnectHandler
import yaml

"""
huawei_AR = {
    'host': '192.168.75.135',
    'device_type': "huawei",
    'username': "huawei",
    'password': "huawei",
}
"""

commands = ["disp ssh server status", "disp ip int br", "disp fan"]

def send_config_commands(device, commands):
    """
    :param device: словарь с параметрами подключения
    :param config_commands: список команд для выполнения
    :return:
    """
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)
        return result


if __name__ == "__main__":
    with open("devices_huawei.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_config_commands(dev, commands))

