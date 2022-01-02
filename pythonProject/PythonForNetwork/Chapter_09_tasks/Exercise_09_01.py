#-------------------------------------------------
"""
"""

"""
    Задание 9.1 - создать функцию, которая генерирует конфигурацию для access портов
    Задание 9.1а - передача параметра port security
"""


access_mode_template = [
        "switchport mode access", "switchport access vlan",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

port_security_template = [
    "switchport port-security",
    "switchport port-security maximum 2",
    "switchport port-security violation restrict"
]

def generate_access_config(intf_vlan_mapping, access_template, portsec=None):
    """
    :param intf_vlan_mapping: словарь с соотвествием интерфейс-VLAN вида:
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17

    :param access_template: список команд для портов в режиме access
    :param portsec: список команд для интерфейсов с портсек
    :return: возвращается список всех портов в режиме access с конфигурацией на основе шаблона
    """

    test_config = []
    for intf, vlan in intf_vlan_mapping.items():
        test_config.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                test_config.append(f"{command} {vlan}")
            else:
                test_config.append(command)
        if portsec:
            test_config.extend(portsec)
    return test_config
