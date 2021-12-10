#-------------------------------------------------
"""
"""

"""
    Задание 5.3,5.3a
    Скрипт должен запрашивать у пользователя:
        * информацию о режиме интерфейса (access/trunk)
        * номере интерфейса (тип и номер, вида Gi0/3)
        * номер VLANа (для режима trunk будет вводиться список VLANов)
    В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться
    соответствующая конфигурация access или trunk (шаблоны команд находятся в списках
    access_template и trunk_template).
    При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем
    соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).
"""
access_template = [                                                                             # кортеж access
        "switchport mode access", "switchport access vlan {}",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
     ]
trunk_template =[                                                                               # кортеж trunk
        "switchport mode trunk","switchport trunk encapsualtion dot1q",
        "switchport trunk allowed vlan {}"
    ]

interface_template = {"access":access_template,"trunk":trunk_template}                          # двумерный список для выбора типа интерфейса
vlans_questions = {"access":"Введите номер VLAN: ", "trunk":"Введите разрешённые VLAN: "}       # двумерный список для выбора описания для VLAN

type_switch_list = ','.join(interface_template.keys())                                          # берем тип интерфейсов для последующего использования в Выборе
type_switch_int = input("Выберетие режим интерфейса ({}): ".format(type_switch_list))           # подставляем тип с помощью format

type_phyz_int = input("Введите тип и номер интерфейса (Fast/Gig): ")
vlans = input(vlans_questions[type_switch_int])                                                 # вводим vlan, описание берется в зависимости от типа access/trunk - соответсвующий элемент ключа списка vlans_questions
print('\n'+'*'*30)
print("Interface {}".format(type_phyz_int))

print('\n'.join(interface_template[type_switch_int]).format(vlans))
print('\n'+'*'*30)

