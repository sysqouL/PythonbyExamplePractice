#-------------------------------------------------
"""
"""

"""
    Задание 9.2 - создать функцию, которая генерирует конфигурацию для trunk портов
    Задание 9.2а - функция должна возвращать не список команд а словарь
"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/03": [120, 130],
    "FastEthernet0/07": [111, 130],
    "FastEthernet0/09": [117],
}

port_security_template = [
    "switchport port-security",
    "switchport port-security maximum 2",
    "switchport port-security violation restrict"
]

def generate_trunk_config(intf_vlan_mapping, trunk_template, portsec=None):
    """
    :param intf_vlan_mapping: словарь с соотвествием интерфейс-VLAN вида:
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
    :param trunk_template: список команд для портов в режиме access
    :param portsec: список команд для интерфейсов с портсек
    :return: возвращается список всех портов в режиме trunk с конфигурацией на основе шаблона
    """

    trunk_test = {}
    for port, vlans in intf_vlan_mapping.items():
        commands = []
        commands.append(f"interface {port}")
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlans_str = ",".join([str(vlan) for vlan in vlans])
                commands.append(f"{command} {vlans_str}")
            else:
                commands.append(f"{command}")
        if portsec:
            commands.extend(portsec)
        trunk_test[port] = commands
    return trunk_test