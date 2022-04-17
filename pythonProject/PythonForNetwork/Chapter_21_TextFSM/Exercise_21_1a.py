#-------------------------------------------------
"""
"""

"""
    Задание 21.1a
    Создать функцию parse_output_to_dict.
    Параметры функции:
    * template - имя файла, в котором находится шаблон TextFSM.
      Например, templates/sh_ip_int_br.template
    * command_output - вывод соответствующей команды show (строка)
    Функция должна возвращать список словарей:
    * ключи - имена переменных в шаблоне TextFSM
    * значения - части вывода, которые соответствуют переменным
    Проверить работу функции на выводе команды output/sh_ip_int_br.txt
    и шаблоне templates/sh_ip_int_br.template.
"""

import textfsm
from pprint import pprint

def parse_output_to_dict(template, command_output):
    with open(template) as f:
        fsm = textfsm.TextFSM(f)
        header = fsm.header
        #print(header)
        result = fsm.ParseText(command_output)
        #pprint(result)
        #test = dict(zip(header,result))
        #pprint(test)
        #print(test)
    return [dict(zip(header, line)) for line in result]


if __name__ == "__main__":
    template = "templates/sh_ip_int_brief_hua.template"             # "templates/sh_ip_int_brief_hua.template"
    with open("output/sh_ip_int_brief_hua.txt") as show:            # "output/sh_ip_int_brief_hua.txt"
        output = show.read()
    result = parse_output_to_dict(template, output)
    pprint(result, width=100)


"""
вариант с ParseTextToDicts
def parse_output_to_dict(template, command_output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        result = fsm.ParseTextToDicts(command_output)
    return result
"""