#-------------------------------------------------
"""
"""

"""
    Задание 6.3 - генератор конфигурации для портов trunk.
"""

access_template = [
    'switchport mode access',
    'switchport access vlan',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport mode trunk',
    'switchport trunk encapsulation dot1q',
    'switchport trunk allowed vlan'
]

access = {'0/12':'10', '0/14':'11', '0/16':'17', '0/17':'150'}
trunk = {'0/1':['add','10','20'], '0/2':['only','11','30'],'0/4':['del','17']}

"""for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")
"""

for intf,action in trunk.items():
    print("Interface FastEthernet " + intf)
    for command in trunk_template:
        if action[0] == "add" and command.endswith("allowed vlan"):
            print(f" {command} {action[0]} {','.join(action[1:3])}")
        elif action[0] == "only" and command.endswith("allowed vlan"):
            print(f" {command} {','.join(action[1:3])}")
        elif action[0] == "del" and command.endswith("allowed vlan"):
            print(f" {command} remove {', '.join(action[1:2])}")
        else:
            print(f" {command}")